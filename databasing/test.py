import database

conn = database.create_connection("databasing/students.db")
database.create_table(conn, "Students", ["first_name 'TEXT'", "last_name 'TEXT'", "age 'INTEGER'", "height 'REAL'"])

#database.insert_db(conn, "Students", ["first_name", "last_name", "age", "height"], ["Tester", "Bester", 17, 1.80])

database.update_db(conn, "Students", ["first_name = 'Mester'", "age = '90'"], "id = '1'")

result = database.select_db(conn, "Students").fetchall()
print(result)

                
                
                
                
                
                try:
                    if any(int(remove_student) in (match := sublist) for sublist in gradebook_list):
                        print(f"Student '{gradebook_list[match.index(int(remove_student))][1]}' was removed.")
                        #student_list.pop(int(remove_student) - 1)
                        database.delete_db(conn, "Students", "id", int(remove_student))
                        break
                    elif remove_student.lower().strip() == "q":
                        break
                    else:
                        print("Invalid student number. Please try again.")
                except IndexError:
                    print("Invalid student number. Please try again.")