import sqlite3
def get_connection():
    return sqlite3.connect("school.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)")
    conn.commit()
    conn.close()
def add_student(name,score):
    create_table()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", (name,score))
    conn.commit()
    conn.close()


def get_students():
    create_table()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    for row in rows :
        print(row)
def search_student(name):
    create_table()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    if len(rows) == 0:
        print("not found")
    else:
        for row in rows:
            print(row)
def delete_student(student_id):
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()
    print("delete done")


