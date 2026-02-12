# Library-Book-Tracker-System
A full-stack library management system with Flask and SQLite. Track books, members, and loans with a clean, responsive web interface.

✨ Features:

📖 Book Management

-Add new books with title, author, ISBN, genre, year, and copy count

-View all books with availability status

-Automatic copy tracking (total vs available)

-Real-time availability indicators

<img width="1823" height="764" alt="Screenshot 2026-02-12 134939" src="https://github.com/user-attachments/assets/f7f3ab19-d770-4ec7-a0c6-de857689c023" />



👥 Member Management

-Register library members with contact details

-View borrowing history and active loans per member

-Automatic join date tracking

-Member activity status

<img width="1696" height="752" alt="Screenshot 2026-02-12 135014" src="https://github.com/user-attachments/assets/aa61fc0a-8d9e-45a4-8b1b-9fc557cb351f" />



📋 Loan System

-Check out books to members (14-day default loan period)

-Return processing with automatic copy count updates

-Overdue detection with color-coded alerts

-Active loans dashboard

<img width="1744" height="646" alt="Screenshot 2026-02-12 135035" src="https://github.com/user-attachments/assets/27013903-03cc-4eb5-a3e4-624d0108f956" />



📊 Dashboard

-Real-time statistics (total books, active members, active loans, overdue)

-Recent loan activity feed

-Quick overview of library status

<img width="1813" height="704" alt="Screenshot 2026-02-12 134910" src="https://github.com/user-attachments/assets/4d2c480b-ec36-472d-8e65-0d5a90b69e1b" />



🛠️ Technology Stack

-Backend: Python 3.8+, Flask

-Database: SQLite 3

-Frontend: HTML5, CSS3

-ORM: Raw SQL (no ORM - pure SQL learning) 

🎯 Key SQL Concepts Demonstrated: 

-CRUD Operations: Create, Read, Update, Delete

-JOINs: Multi-table queries (books × loans × members)

-Aggregations: COUNT, SUM with GROUP BY

-Subqueries: Nested queries for complex filtering

-Date Functions: Due date calculations, overdue detection

-Transactions: Atomic operations for check-out/return

-Indexing: Primary keys and foreign key relationships

🎓 Learning Outcomes

-By studying this project, you'll learn:

-Database Design - Normalized schema with relationships

-SQL Queries - Complex JOINs, aggregations, subqueries

-Web Development - Flask routes, request handling, templates

-CRUD Operations - Complete data lifecycle management

-State Management - Tracking book availability across transactions

-Date/Time Handling - Due dates, overdue calculations

Happy Coding! 🚀



