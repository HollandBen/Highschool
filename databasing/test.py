import database

conn = database.create_connection("databasing/students.db")
database.create_table(conn, "Students", ["first_name 'TEXT'", "last_name 'TEXT'", "age 'INTEGER'", "height 'REAL'"])

#database.insert_db(conn, "Students", ["first_name", "last_name", "age", "height"], ["Tester", "Bester", 17, 1.80])

database.update_db(conn, "Students", ["first_name = 'Mester'", "age = '90'"], "id = '1'")

result = database.select_db(conn, "Students").fetchall()
print(result)