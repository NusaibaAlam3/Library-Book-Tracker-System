import sqlite3
import os

def init_database():
    # Remove existing database if any
    if os.path.exists('library.db'):
        os.remove('library.db')
    
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    # Create Books table
    cursor.execute('''
        CREATE TABLE books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE,
            genre TEXT,
            published_year INTEGER,
            total_copies INTEGER DEFAULT 1,
            available_copies INTEGER DEFAULT 1
        )
    ''')
    
    # Create Members table
    cursor.execute('''
        CREATE TABLE members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE,
            phone TEXT,
            join_date DATE DEFAULT CURRENT_DATE,
            active BOOLEAN DEFAULT 1
        )
    ''')
    
    # Create Loans table
    cursor.execute('''
        CREATE TABLE loans (
            loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER,
            member_id INTEGER,
            loan_date DATE DEFAULT CURRENT_DATE,
            due_date DATE,
            return_date DATE,
            status TEXT DEFAULT 'active',
            FOREIGN KEY (book_id) REFERENCES books (book_id),
            FOREIGN KEY (member_id) REFERENCES members (member_id)
        )
    ''')
    
    # Insert sample data 
    sample_books = [
    # Bangladeshi Literature
    ('Debi', 'Humayun Ahmed', '9789845023456', 'Mystery', 1995, 4, 3),
    ('Himu', 'Humayun Ahmed', '9789845023463', 'Fiction', 1993, 3, 2),
    ('Lalsalu', 'Syed Waliullah', '9789845023470', 'Literary Fiction', 1948, 2, 1),
    ('Krishnopokkho', 'Sunil Gangopadhyay', '9789845023487', 'Historical', 1986, 3, 2),
    ('Chander Pahar', 'Bibhutibhushan Bandyopadhyay', '9789845023494', 'Adventure', 1937, 3, 1),
    
    # Classics
    ('Wuthering Heights', 'Emily Brontë', '9780141439556', 'Gothic Romance', 1847, 3, 2),
    ('Jane Eyre', 'Charlotte Brontë', '9780141441146', 'Romance', 1847, 2, 1),
    ('David Copperfield', 'Charles Dickens', '9780141439440', 'Classic', 1850, 2, 2),
    ('Anna Karenina', 'Leo Tolstoy', '9780143035008', 'Literary Fiction', 1878, 2, 1),
    ('The Count of Monte Cristo', 'Alexandre Dumas', '9780140449266', 'Adventure', 1844, 3, 2),
    
    # Science Fiction
    ('Dune', 'Frank Herbert', '9780441013593', 'Science Fiction', 1965, 4, 3),
    ('Foundation', 'Isaac Asimov', '9780553293357', 'Science Fiction', 1951, 3, 2),
    ('Neuromancer', 'William Gibson', '9780441569595', 'Cyberpunk', 1984, 2, 1),
    ('The Left Hand of Darkness', 'Ursula K. Le Guin', '9780441478125', 'Sci-Fi', 1969, 2, 2),
    ('Snow Crash', 'Neal Stephenson', '9780553380958', 'Cyberpunk', 1992, 2, 1),
    
    # History & Historical Fiction
    ('Guns, Germs, and Steel', 'Jared Diamond', '9780393354324', 'History', 1997, 3, 2),
    ('Sapiens', 'Yuval Noah Harari', '9780062316097', 'History', 2011, 5, 4),
    ('The Silk Roads', 'Peter Frankopan', '9781101912379', 'History', 2015, 3, 2),
    ('The Guns of August', 'Barbara W. Tuchman', '9780345476098', 'Military History', 1962, 2, 1),
    ('1776', 'David McCullough', '9780743226721', 'History', 2005, 2, 2),
    
    # Mystery & Thriller
    ('And Then There Were None', 'Agatha Christie', '9780062073488', 'Mystery', 1939, 4, 3),
    ('The Hound of the Baskervilles', 'Arthur Conan Doyle', '9780140437867', 'Detective', 1902, 3, 2),
    ('The Girl with the Dragon Tattoo', 'Stieg Larsson', '9780307949486', 'Thriller', 2005, 3, 2),
    ('Gone Girl', 'Gillian Flynn', '9780307588364', 'Psychological Thriller', 2012, 2, 1),
    ('The Silent Patient', 'Alex Michaelides', '9781250301697', 'Psychological Thriller', 2019, 4, 3),
    
    # Fantasy & Mythology
    ('The Name of the Wind', 'Patrick Rothfuss', '9780756404741', 'Fantasy', 2007, 3, 2),
    ('American Gods', 'Neil Gaiman', '9780062572233', 'Fantasy', 2001, 2, 1),
    ('The Ocean at the End of the Lane', 'Neil Gaiman', '9780062459367', 'Fantasy', 2013, 2, 2),
    ('Circe', 'Madeline Miller', '9780316556323', 'Mythology', 2018, 3, 2),
    ('The Song of Achilles', 'Madeline Miller', '9780062060624', 'Mythology', 2011, 3, 2)
]
    

    cursor.executemany('''
        INSERT INTO books (title, author, isbn, genre, published_year, total_copies, available_copies)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', sample_books)
    
    sample_members = [
    ('Ananna', 'Debnath', 'ananna.d@email.com', '555-0105', '2024-01-15'),
    ('Nusrat', 'Jahan', 'nusrat.j@email.com', '555-0106', '2024-01-18'),
    ('Nobin', 'Alam', 'nobin.a@email.com', '555-0107', '2024-01-20'),
    ('Syeda', 'Nasmina', 'syeda.n@email.com', '555-0108', '2024-01-22'),
    ('Simran', 'Khan', 'simran.k@email.com', '555-0109', '2024-01-25'),
    ('Shamsul', 'Shanto', 'shamsul.s@email.com', '555-0110', '2024-01-28'),
    ('Imran', 'Hossain', 'imran.h@email.com', '555-0111', '2024-02-01'),
    ('Farhana', 'Islam', 'farhana.i@email.com', '555-0112', '2024-02-03'),
    ('Tanvir', 'Ahmed', 'tanvir.a@email.com', '555-0113', '2024-02-05'),
    ('Rafiq', 'Uddin', 'rafiq.u@email.com', '555-0114', '2024-02-07'),
    ('Sharmin', 'Akter', 'sharmin.a@email.com', '555-0115', '2024-02-10'),
    ('Hasan', 'Mahmud', 'hasan.m@email.com', '555-0116', '2024-02-12'),
    ('Tahmina', 'Rahman', 'tahmina.r@email.com', '555-0117', '2024-02-14'),
    ('Sohel', 'Rana', 'sohel.r@email.com', '555-0118', '2024-02-16'),
    ('Moumita', 'Sen', 'moumita.s@email.com', '555-0119', '2024-02-18'),
    ('Ashik', 'Islam', 'ashik.i@email.com', '555-0120', '2024-02-20'),
    ('Rumana', 'Akhtar', 'rumana.a@email.com', '555-0121', '2024-02-22'),
    ('Parvez', 'Hasan', 'parvez.h@email.com', '555-0122', '2024-02-24'),
    ('Shamima', 'Sultana', 'shamima.s@email.com', '555-0123', '2024-02-26'),
    ('Mehedi', 'Hasan', 'mehedi.h@email.com', '555-0124', '2024-02-28')
]
    
    cursor.executemany('''
        INSERT INTO members (first_name, last_name, email, phone, join_date)
        VALUES (?, ?, ?, ?, ?)
    ''', sample_members)
    
    # Sample loans
    sample_loans = [
        (1, 1, '2024-02-01', '2024-02-15', None, 'active'),
        (2, 2, '2024-02-05', '2024-02-19', None, 'active'),
        (5, 3, '2024-02-10', '2024-02-24', None, 'active')
    ]
    
    cursor.executemany('''
        INSERT INTO loans (book_id, member_id, loan_date, due_date, return_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', sample_loans)
    
    conn.commit()
    conn.close()
    print("Database initialized successfully!")

if __name__ == '__main__':
    init_database()