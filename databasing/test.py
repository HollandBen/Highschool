import database

conn = database.create_connection("databasing/students.db")
database.create_table(conn, "Students", ["first_name 'TEXT'", "last_name 'TEXT'", "age 'INTEGER'", "height, 'REAL'"])