import psycopg2 as p

# reading config file for database name, username and password
def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key.strip()] = value.strip()
    return config

# get students info
def get_students(cursor):
    cursor.execute("SELECT * FROM students")
    print(cursor.fetchall())

# add student to db
def add_student(cursor, first_name, last_name, email, enrollment_date):
    cursor.execute(f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')")

# update student email by id
def update_email(cursor, student_id, new_email):
    cursor.execute(f"UPDATE students set email = '{new_email}' WHERE student_id = '{student_id}'")

# delete student by id
def delete_student(cursor, student_id):
    cursor.execute(f"DELETE FROM students WHERE student_id = '{student_id}'")

# please update the config.txt file with the databases' name username password
config = read_config('config.txt')
database = config.get('database')
username = config.get('username')
password = config.get('password')

conn = p.connect(dbname=database, user=username, password=password, host='localhost', port=5432)
cursor = conn.cursor()

selection = ""

while selection == "" or selection[0] != "e":
    selection = input("Input your selection:\n\n  get students\n  add student\n  update student's email\n  delete student\n  exit\n\n")

    if selection[0] == "g":
        get_students(cursor)

    if selection[0] == "a":
        first = input("Input student's first name: ")
        last = input("Input student's last name: ")
        email = input("Input email: ")
        date = input("Input the enrollment date in the format YYYY-MM-DD: ")
        add_student(cursor, first, last, email, date)

    if selection[0] == "u":
        id = input("Input the student id of the email to update: ")
        email = input("Input the new email: ")
        update_email(cursor, id, email)

    if selection[0] == "d":
        id = input("Input the id of the student to delete: ")
        delete_student(cursor, id)

cursor.close()
conn.commit()
conn.close()