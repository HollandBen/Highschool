#Ben Holland
#26 March 2024
#Student grades program v2.0 (database ver.)

#to do:
    #bug test the adding a new student command, make sure it errors properly
    #the class list needs to update properly after
    #give feedback that the student and their grades were added
    #work on commands listed as "NEED FIX"

#database starter
import database
conn = database.create_connection("databasing/gradebook.db")
database.create_table(conn, "Students", ["name 'TEXT'", "assign_1 'REAL'", "assign_2 'REAL'", "assign_3 'REAL'", "assign_4 'REAL'", "assign_5 'REAL'"])

#database.insert_db(conn, "Students", ["name", "assign_1", "assign_2", "assign_3", "assign_4", "assign_5"], ["Danielle", 90, 92, 91, 99, 0])
#database.update_db(conn, "Students", ["first_name = 'Mester'", "age = '90'"], "id = '1'")

result = database.select_db(conn, "Students").fetchall()

#important variables
border = "----------------------------------------\n"

#creates 2d array (now with id)
gradebook_list = [list(ele) for ele in result]

student_list_length = len(gradebook_list)

#main menu function
def main_menu():
    while True:
        print(border)
        print("Main Menu\nEnter 'mean' to receive the class mean or enter 'students' to access grade information. To make changes to the class list, enter 'edit'.\nEnter 'Q' to exit the program.")
        call_main_menu = input("> Enter input: ").lower().strip()
        
        #command to get the class average
        if call_main_menu == "mean":
            class_mean()

        #enter edit class menu
        elif call_main_menu == "edit":
            edit_student()
            
        #enter individual student menu
        elif call_main_menu == "students":
            student_menu()
        
        #exit program completely
        elif call_main_menu == "q":
            break
        
        #error
        else:
            print("An unexpected value was received. Please try again.")

#simple to get the class mean
def class_mean():
    class_total = 0
    for i in range(0, student_list_length):
        class_adder = sum(gradebook_list[i][2:])
        assignments_list = len(gradebook_list[i])
        try:
            class_adder = class_adder / (assignments_list - 2)
        except ZeroDivisionError:
            class_adder = 0
        class_total += class_adder
    class_average = class_total / student_list_length
    print(border)
    print(f"The class average is: {round(class_average, 2)} %.")

#editing the student list function
def edit_student():
    while True:
        global gradebook_list, student_list_length
        student_list_length = len(gradebook_list)
        gradebook_list.sort()
        print(border)
        print("Class list:")
        for i in range(0, student_list_length):
            print(i + 1, gradebook_list[i][1])
        print("Enter 'add' to add a student to the list or enter 'remove' to remove a student from the list.\nEnter 'Q' to return to the main menu.")
        edit_student_choice = input("> Enter input: ").lower().strip()
        
        #FIX ADDING
        #command for adding a new student to the class list
        if edit_student_choice == "add":
            print(border)
            print("Enter the new student's name.\nEnter 'Q' to return to the student editor menu.")
            breaker = False
            while True:
                new_student_name = input("> Enter input: ")
                if new_student_name.isdigit():
                    print("Invalid name. Please try again.")
                elif new_student_name.lower().strip() == "q":
                    break
                elif breaker:
                    break
                else:
                    new_student_name.strip().capitalize()
                    print(f"Student '{new_student_name}' was added.")
                    print("Enter the five assignment grades associated with this student. Use the format: xx, xx, xx, xx, xx\nEnter 'Q' to return to the adding student menu.")
                    while True:
                        call_adding_items = input("> Enter input: ")
                        if call_adding_items.lower().strip() == "q":
                            breaker = True
                            break
                        else:
                            try:
                                new_grade_1, new_grade_2, new_grade_3, new_grade_4, new_grade_5 = call_adding_items.split(", ")
                                database.insert_db(conn, "Students", ["name", "assign_1", "assign_2", "assign_3", "assign_4", "assign_5"], [new_student_name, float(new_grade_1), float(new_grade_2), float(new_grade_3), float(new_grade_4), float(new_grade_5)])
                                #student_list.append([new_student_name])
                                breaker = True
                                break
                            except TypeError:
                                print("Invalid input. Please try again.")
        
        #FIX REMOVING
        #command for removing a student from the class list
        elif edit_student_choice == "remove":
            print(border)
            print("Enter the student's number to remove them from the list.\nEnter 'Q' to return to the student editor menu.")
            while True:
                remove_student = input("> Enter input: ")
                if remove_student.isdigit() and int(remove_student) <= student_list_length and int(remove_student) >= 1:
                    print(f"Student '{student_list[int(remove_student) - 1][0]}' was removed.")
                    student_list.pop(int(remove_student) - 1)
                    break
                elif remove_student.lower().strip() == "q":
                    break
                else:
                    print("Invalid student number. Please try again.")
        
        #command for exiting the current menu and returning to the main menu
        elif edit_student_choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")

#editing one of the students from the class list
def student_menu():
    while True:
        global student_average, gradebook_list
        print(border)
        print("Class list:")
        for i in range(0, student_list_length):
            print(i + 1, gradebook_list[i][1])
        print("Enter the student's number to access their profile.\nEnter 'Q' to return to the main menu.")
        student_menu_choice = input("> Enter input: ")
        
        #checks to make sure that the student number that was entered is a valid part of the class
        if student_menu_choice.isdigit() and int(student_menu_choice) <= student_list_length and int(student_menu_choice) >= 1:
            while True:
                print(border)
                print(f"Student selected: {gradebook_list[int(student_menu_choice) - 1][1]}")
                assignments_list = len(gradebook_list[int(student_menu_choice) - 1])
                print("The recorded grades for this student are:")
                for i in range(2, assignments_list):
                    print(f"Assignment {i}: {(gradebook_list[int(student_menu_choice) - 1][i])} %")
                print("Enter 'mean' to get this student's average, enter 'add' to add an assignment's grade to their progile, or enter 'remove' to remove an assignment.\nEnter 'Q' to return to student grade information menu.")
                individual_choice = input("> Enter input: ")
                
                #gets the mean of the student's grades
                if individual_choice.strip().lower() == "mean":
                    student_adder = sum(gradebook_list[int(student_menu_choice) - 1][2:])
                    try:
                        student_average = student_adder / (assignments_list - 2)
                    except ZeroDivisionError:
                        student_average = 0
                    print(border)
                    print(f"The student's average is: {round(student_average, 2)} %.")
                
                #NEEDS FIX
                #command to add a new assignment to the student's grades (in percent)
                elif individual_choice.strip().lower() == "add":
                    print(border)
                    print(r"Enter the new percentage grade to be added. Grades between 0 % and 115 % are accepted.")
                    new_grade = input("> Enter input: ")
                    try:
                        if float(new_grade) >= 0 and float(new_grade) <= 115:
                            student_list[int(student_menu_choice) - 1].append(round(float(new_grade), 2))
                        else:
                            print("Invalid grade. Please try again.")
                    except ValueError:
                        print("Invalid grade. Please try again.")
                
                #NEEDS FIX
                #command to remove an assignment from the student's grades
                elif individual_choice.strip().lower() == "remove":
                    print(border)
                    print("Enter the assignment number to be removed.")
                    delete_grade = input("> Enter input: ")
                    
                    #checks that the grade does exist in the assignments list
                    if delete_grade.isdecimal() and int(delete_grade) >= 1 and int(delete_grade) < assignments_list:
                        print(f"Grade '{student_list[int(student_menu_choice) - 1][int(delete_grade)]}' was removed")
                        del student_list[int(student_menu_choice) - 1][int(delete_grade)]
                    else:
                        print("Invalid choice. Please try again.")
                
                #command for exiting the current menu and returning to the previous menu
                elif individual_choice.strip().lower() == "q":
                    break
                else:
                    print("Invalid choice. Please try again.")
        
        #command for exiting the current menu and returning to the main menu
        elif student_menu_choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")


#loop that actually runs the program constantly            
main_menu()

#STUDENTS > [X] (BROKEN)