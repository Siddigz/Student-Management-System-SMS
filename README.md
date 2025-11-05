# Student Management System (SMS)

**Name:** Siddig Ahmed  
**Student ID:** 101332539  
**Course:** COMP 3005

A small Python program that connects to a database and performs CRUD operations for student records.

## Features
- List all students
- Add a new student
- Update a student's email by their id
- Delete a student record by their id

## Functions (API)
- `connect()` — Connects to postgres server.  
- `get_all_students()` — Retrieve and return all student records.  
- `add_student(first_name, last_name, email, enrollment_date)` — Insert a new student.  
- `update_student_email(student_id, new_email)` — Update email for a student by ID.  
- `delete_student(student_id)` — Remove a student record by ID.

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/Siddigz/Student-Management-System-SMS.git
    ```
2. Navigate to the directory:
    ```
    cd .\Student-Management-System-SMS\
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```


## Running the Application

1. Prerequisites
    - Python 3.8+ and pip
    - PostgreSQL server running and accessible

2. Configure the database connection in app.py
      ```
        DB_USER = "postgres"
        DB_PASS = "sql123"
        DB_HOST = "localhost"
        DB_PORT = "5432" 
      ```

3. Create the database and table (if not done already)
    - Create the students table according to database.sql file

4. Run the application
    - Start the program using:
      ```
      py main.py
      ```

## Video demonstration
YouTube: https://youtube.com


