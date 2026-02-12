from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
DATABASE = 'library.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Home Dashboard
@app.route('/')
def index():
    conn = get_db()
    
    # Get statistics
    total_books = conn.execute('SELECT COUNT(*) as count FROM books').fetchone()['count']
    total_members = conn.execute('SELECT COUNT(*) as count FROM members WHERE active = 1').fetchone()['count']
    active_loans = conn.execute('SELECT COUNT(*) as count FROM loans WHERE status = "active"').fetchone()['count']
    overdue_loans = conn.execute('''
        SELECT COUNT(*) as count FROM loans 
        WHERE status = "active" AND due_date < DATE("now")
    ''').fetchone()['count']
    
    # Get recent loans
    recent_loans = conn.execute('''
        SELECT l.loan_id, b.title, m.first_name || " " || m.last_name as member_name,
               l.loan_date, l.due_date, l.status
        FROM loans l
        JOIN books b ON l.book_id = b.book_id
        JOIN members m ON l.member_id = m.member_id
        ORDER BY l.loan_date DESC
        LIMIT 5
    ''').fetchall()
    
    conn.close()
    
    return render_template('index.html', 
                         total_books=total_books,
                         total_members=total_members,
                         active_loans=active_loans,
                         overdue_loans=overdue_loans,
                         recent_loans=recent_loans)

# Books Management
@app.route('/books')
def books():
    conn = get_db()
    books = conn.execute('''
        SELECT *, 
               CASE WHEN available_copies > 0 THEN 'Available' ELSE 'Checked Out' END as status
        FROM books 
        ORDER BY title
    ''').fetchall()
    conn.close()
    return render_template('books.html', books=books)

@app.route('/books/add', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    isbn = request.form['isbn']
    genre = request.form['genre']
    year = request.form['published_year']
    copies = request.form['total_copies']
    
    conn = get_db()
    try:
        conn.execute('''
            INSERT INTO books (title, author, isbn, genre, published_year, total_copies, available_copies)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, author, isbn, genre, year, copies, copies))
        conn.commit()
        flash('Book added successfully!', 'success')
    except sqlite3.IntegrityError:
        flash('Book with this ISBN already exists!', 'error')
    finally:
        conn.close()
    
    return redirect(url_for('books'))

# Members Management
@app.route('/members')
def members():
    conn = get_db()
    members = conn.execute('''
        SELECT m.*, 
               COUNT(l.loan_id) as books_borrowed,
               SUM(CASE WHEN l.status = "active" THEN 1 ELSE 0 END) as active_loans
        FROM members m
        LEFT JOIN loans l ON m.member_id = l.member_id
        WHERE m.active = 1
        GROUP BY m.member_id
        ORDER BY m.last_name
    ''').fetchall()
    conn.close()
    return render_template('members.html', members=members)

@app.route('/members/add', methods=['POST'])
def add_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    
    conn = get_db()
    try:
        conn.execute('''
            INSERT INTO members (first_name, last_name, email, phone)
            VALUES (?, ?, ?, ?)
        ''', (first_name, last_name, email, phone))
        conn.commit()
        flash('Member added successfully!', 'success')
    except sqlite3.IntegrityError:
        flash('Email already registered!', 'error')
    finally:
        conn.close()
    
    return redirect(url_for('members'))

# Loans Management
@app.route('/loans')
def loans():
    conn = get_db()
    
    # Get active loans
    active_loans = conn.execute('''
        SELECT l.loan_id, b.book_id, b.title, b.author,
               m.member_id, m.first_name, m.last_name,
               l.loan_date, l.due_date,
               julianday(l.due_date) - julianday('now') as days_remaining
        FROM loans l
        JOIN books b ON l.book_id = b.book_id
        JOIN members m ON l.member_id = m.member_id
        WHERE l.status = 'active'
        ORDER BY l.due_date
    ''').fetchall()
    
    # Get available books for new loans
    available_books = conn.execute('''
        SELECT * FROM books 
        WHERE available_copies > 0 
        ORDER BY title
    ''').fetchall()
    
    # Get active members
    active_members = conn.execute('''
        SELECT * FROM members 
        WHERE active = 1 
        ORDER BY last_name
    ''').fetchall()
    
    conn.close()
    return render_template('loans.html', 
                         active_loans=active_loans,
                         available_books=available_books,
                         active_members=active_members)

@app.route('/loans/create', methods=['POST'])
def create_loan():
    book_id = request.form['book_id']
    member_id = request.form['member_id']
    due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
    
    conn = get_db()
    
    # Check if book is available
    book = conn.execute('SELECT available_copies FROM books WHERE book_id = ?', (book_id,)).fetchone()
    
    if book and book['available_copies'] > 0:
        # Create loan
        conn.execute('''
            INSERT INTO loans (book_id, member_id, due_date)
            VALUES (?, ?, ?)
        ''', (book_id, member_id, due_date))
        
        # Update available copies
        conn.execute('''
            UPDATE books 
            SET available_copies = available_copies - 1 
            WHERE book_id = ?
        ''', (book_id,))
        
        conn.commit()
        flash('Book checked out successfully!', 'success')
    else:
        flash('Book is not available!', 'error')
    
    conn.close()
    return redirect(url_for('loans'))

@app.route('/loans/return/<int:loan_id>')
def return_book(loan_id):
    conn = get_db()
    
    # Get book_id from loan
    loan = conn.execute('SELECT book_id FROM loans WHERE loan_id = ?', (loan_id,)).fetchone()
    
    if loan:
        # Update loan
        conn.execute('''
            UPDATE loans 
            SET return_date = DATE('now'), status = 'returned'
            WHERE loan_id = ?
        ''', (loan_id,))
        
        # Update book availability
        conn.execute('''
            UPDATE books 
            SET available_copies = available_copies + 1 
            WHERE book_id = ?
        ''', (loan['book_id'],))
        
        conn.commit()
        flash('Book returned successfully!', 'success')
    
    conn.close()
    return redirect(url_for('loans'))

if __name__ == '__main__':
    app.run(debug=True)