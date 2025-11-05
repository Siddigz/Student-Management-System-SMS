import psycopg2 

# DB_NAME = "siddigz-server"
DB_USER = "postgres"
DB_PASS = "sql123"
DB_HOST = "localhost"
DB_PORT = "5432" 

'''
    Connects to a SQL server
'''
def connect():
    # Sets variables used throughout code to global
    global connection
    global cursor

    try:
        # Connects to server through provided data
        connection = psycopg2.connect(
            user = DB_USER,
            password = DB_PASS,
            host = DB_HOST,
            port = DB_PORT
            )
        
        print("\nConnected to the database successfully!")

    except psycopg2.Error as e:
        # Displays error
        print(f"\nConnection error: \n\t{e}")
        connection = None

    # Defines cursor which will be used to execute server commands
    cursor = connection.cursor()

'''
    Displays all the student records to the terminal
'''
def getAllStudents():
    print("\ngetAllStudents():")
    
    try:
        # Runs SELECT command in the server
        cursor.execute("SELECT * FROM students ORDER BY student_id;")

        # Stores info gotten into a students array
        students = cursor.fetchall()

        print("\tID | First Name | Last Name | Email | Enrollment Date")
        print("\t" + "-" * 50)

        # Loads info from each student
        for student in students:
            print(f"\t{student[0]} | {student[1]} | {student[2]} | {student[3]} | {student[4]}")

    except Exception as e:
        # Displays error
        print(f"Error: \n\t{e}")

'''
    Adds a student record to the database
'''   
def addStudent(first_name, last_name, email, enrollment_date):
    print("\naddStudent():")
    
    try:
        # Runs INSERT command in the server
        cursor.execute(f"""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')""")

        print(f"\tAdded {first_name} successfully!")

    except Exception as e:
        # Displays error
        print(f"Error: \n\t{e}")

'''
    Updates the email of a student in the student record
'''
def updateStudentEmail(student_id, new_email): 
    print("\nupdateStudentEmail():")
    
    try:
        # Runs UPDATE command in the server
        cursor.execute(f"""UPDATE students SET email = '{new_email}' WHERE student_id = {student_id};""")

        print(f"\tUpdated ID_{student_id}'s email to {new_email} successfully!")

    except Exception as e:
        # Displays error
        print(f"Error: \n\t{e}")

'''
    Deletes a student of the student record
'''
def deleteStudent(student_id): 
    print("\ndeleteStudent():")
    
    try:
        # Runs DELETE command in the server
        cursor.execute(f"""DELETE FROM students WHERE student_id = {student_id};""")

        print(f"\tDeleted ID_{student_id} successfully!")

    except Exception as e:
        print(f"Error: \n\t{e}")

'''
    Example Workflow
'''
def main():
    # Runs predefined examples

    getAllStudents()

    # Adds 2 students
    addStudent("Siddig", "Ahmed", "siddig@email.com", "2024-09-01")
    addStudent("Van", "Diseal", "van@email.com", "2025-09-01")

    getAllStudents()

    # Deletes student with id of 3
    deleteStudent(3)
    
    getAllStudents()

    # Updates 2 student emails
    updateStudentEmail(1, "johnny@email.com")
    updateStudentEmail(2, "janet@email.com")

    getAllStudents()

if __name__ == "__main__":
    # Opens server connection
    connect()

    main()

    # Closes server connection
    connection.close()