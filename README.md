# Library-Book-Tracker-System
A full-stack library management system with Flask and SQLite. Track books, members, and loans with a clean, responsive web interface.

✨ Features:
📖 Book Management
Add new books with title, author, ISBN, genre, year, and copy count
View all books with availability status
Automatic copy tracking (total vs available)
Real-time availability indicators

👥 Member Management
Register library members with contact details
View borrowing history and active loans per member
Automatic join date tracking
Member activity status

📋 Loan System
Check out books to members (14-day default loan period)
Return processing with automatic copy count updates
Overdue detection with color-coded alerts
Active loans dashboard

📊 Dashboard
Real-time statistics (total books, active members, active loans, overdue)
Recent loan activity feed
Quick overview of library status

🛠️ Technology Stack
Backend: Python 3.8+, Flask
Database: SQLite 3
Frontend: HTML5, CSS3
ORM: Raw SQL (no ORM - pure SQL learning) 

🎯 Key SQL Concepts Demonstrated: 
CRUD Operations: Create, Read, Update, Delete
JOINs: Multi-table queries (books × loans × members)
Aggregations: COUNT, SUM with GROUP BY
Subqueries: Nested queries for complex filtering
Date Functions: Due date calculations, overdue detection
Transactions: Atomic operations for check-out/return
Indexing: Primary keys and foreign key relationships

🎓 Learning Outcomes
By studying this project, you'll learn:
Database Design - Normalized schema with relationships
SQL Queries - Complex JOINs, aggregations, subqueries
Web Development - Flask routes, request handling, templates
CRUD Operations - Complete data lifecycle management
State Management - Tracking book availability across transactions
Date/Time Handling - Due dates, overdue calculations

Happy Coding! 🚀



