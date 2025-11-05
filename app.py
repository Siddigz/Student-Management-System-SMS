import psycopg2 

DB_NAME = "siddigz-server"
DB_USER = "postgres"
DB_PASS = "sql123"
DB_HOST = "localhost"
DB_PORT = "5432" 

def getAllStudents():
    print("\ngetAllStudents():")
    
    try:
        cursor.execute("SELECT * FROM students ORDER BY student_id;")

        students = cursor.fetchall()

        print("ID | First Name | Last Name | Email | Enrollment Date")
        print("-" * 60)

        for student in students:
            print(f"{student[0]} | {student[1]} | {student[2]} | {student[3]} | {student[4]}")

    except Exception as e:
        print(f"Error: \n{e}")
        
def addStudent(first_name, last_name, email, enrollment_date):
    print("\naddStudent():")
    
    try:
        cursor.execute(f"""INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')""")

        print(f"Added {first_name} successfully!")

    except Exception as e:
        print(f"Error: \n{e}")

def updateStudentEmail(student_id, new_email): 
    print("\nupdateStudentEmail():")
    
    try:
        cursor.execute(f"""UPDATE students SET email = '{new_email}' WHERE student_id = {student_id};""")

        print(f"Updated ID_{student_id}'s email to {new_email} successfully!")

    except Exception as e:
        print(f"Error: \n{e}")

def deleteStudent(student_id): 
    print("\ndeleteStudent():")
    
    try:
        cursor.execute(f"""DELETE FROM students WHERE student_id = {student_id};""")

        print(f"Deleted ID_{student_id} successfully!")

    except Exception as e:
        print(f"Error: \n{e}")

def connect():
    global connection
    global cursor

    try:
        connection = psycopg2.connect(
            user = DB_USER,
            password = DB_PASS,
            host = DB_HOST,
            port = DB_PORT
            )
        
        print("\nConnected to the database successfully!")

    except psycopg2.Error as e:

        print(f"\nConnection error: \n{e}")
        connection = None

    cursor = connection.cursor()

def main():
    getAllStudents()

    addStudent("Siddig", "Ahmed", "siddig@email.com", "2024-09-01")
    addStudent("Van", "Ahmed", "van@email.com", "2024-09-01")

    getAllStudents()

    deleteStudent(3)
    
    getAllStudents()

    updateStudentEmail(1, "johnny@email.com")
    updateStudentEmail(1, "janet@email.com")

    getAllStudents()


if __name__ == "__main__":
    connect()
    main()
    connection.close()