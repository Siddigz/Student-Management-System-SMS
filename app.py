import psycopg2 

DB_NAME = "siddigz-server"
DB_USER = "postgres"
DB_PASS = "sql123"
DB_HOST = "localhost"
DB_PORT = "5432" 


def getAllStudents():
    """Retrieves and displays all records from the students table."""
    print("\ngetAllStudents() Results:")

    global connection

    try:
        cursor_obj = connection.cursor()

        cursor_obj.execute("SELECT * FROM students;")

        students = cursor_obj.fetchall()

        print("ID | First Name | Last Name | Email | Enrollment Date")
        print("-" * 60)

        for student in students:
            print(f"{student[0]} | {student[1]:<10} | {student[2]:<9} | {student[3]:<20} | {student[4]}")

    except Exception as e:
        print(f"Error retrieving students: {e}")
        

def addStudent(first_name, last_name, email, enrollment_date):
    pass

def updateStudentEmail(student_id, new_email): 
    pass

def deleteStudent(student_id): 
    pass

def main():
    global connection

    try:
        connection = psycopg2.connect(
            user = DB_USER,
            password = DB_PASS,
            host = DB_HOST,
            port = DB_PORT
            )
        
        print("Connected to the database successfully!")

    except psycopg2.Error as e:

        print(f"Error connecting to the database: \n{e}")
        connection = None


    
    getAllStudents()



    connection.close()

if __name__ == "__main__":
    main()