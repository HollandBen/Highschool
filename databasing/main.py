#Ben Holland
#26 March 2024
#Student grades program v2.0 (database ver.)

import database
conn = database.create_connection("databasing/gradebook.db")
database.create_table(conn, "Students", ["name 'TEXT'", "assign_1 'REAL'", "assign_2 'REAL'", "assign_3 'REAL'", "assign_4 'REAL'", "assign_5 'REAL'"])

database.insert_db(conn, "Students", ["name", "assign_1", "assign_2", "assign_3", "assign_4", "assign_5"], ["Danielle", 90, 92, 91, 99, 0])

student_list = [
    ["Alex", 98, 99, 97, 100, 102],
    ["Brett", 64, 73, 50, 0, 20],
    ["Edith", 40, 65, 39, 57],
    ["Caden", 85, 89, 78, 91, 91],
    ["Danielle", 90, 92, 91, 99]
]

#database.update_db(conn, "Students", ["first_name = 'Mester'", "age = '90'"], "id = '1'")

result = database.select_db(conn, "Students").fetchall()
print(result)