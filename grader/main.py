#Ben Holland
#28 Feb 2024
#Student grades program

#important variables
border = "----------------------------------------\n"
student_list = [
    ["Alex", 98, 99, 97, 100, 102],
    ["Brett", 64, 73, 50, 0, 20],
    ["Edith", 40, 65, 39, 57],
    ["Caden", 85, 89, 78, 91, 91],
    ["Danielle", 90, 92, 91, 99]
]
student_list_length = len(student_list)

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
        class_adder = sum(student_list[i][1:])
        assignments_list = len(student_list[i])
        try:
            class_adder = class_adder / (assignments_list - 1)
        except ZeroDivisionError:
            class_adder = 0
        class_total += class_adder
    class_average = class_total / student_list_length
    print(border)
    print(f"The class average is: {round(class_average, 2)} %.")

#editing the student list function
def edit_student():
    while True:
        global student_list, student_list_length
        student_list_length = len(student_list)
        student_list.sort()
        print(border)
        print("Class list:")
        for i in range(0, student_list_length):
            print(i + 1, student_list[i][0])
        print("Enter 'add' to add a student to the list or enter 'remove' to remove a student from the list.\nEnter 'Q' to return to the main menu.")
        edit_student_choice = input("> Enter input: ").lower().strip()
        
        #command for adding a new student to the class list
        if edit_student_choice == "add":
            print(border)
            print("Enter the new student's name.\nEnter 'Q' to return to the student editor menu.")
            while True:
                new_student_name = input("> Enter input: ")
                if new_student_name.isdigit():
                    print("Invalid name. Please try again.")
                elif new_student_name.lower().strip() == "q":
                    break
                else:
                    new_student_name.strip().capitalize()
                    print(f"Student '{new_student_name}' was added.")
                    student_list.append([new_student_name])
                    break
        
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
        global student_average, student_list
        print(border)
        print("Class list:")
        for i in range(0, student_list_length):
            print(i + 1, student_list[i][0])
        print("Enter the student's number to access their profile.\nEnter 'Q' to return to the main menu.")
        student_menu_choice = input("> Enter input: ")
        
        #checks to make sure that the student number that was entered is a valid part of the class
        if student_menu_choice.isdigit() and int(student_menu_choice) <= student_list_length and int(student_menu_choice) >= 1:
            while True:
                print(border)
                print(f"Student selected: {student_list[int(student_menu_choice) - 1][0]}")
                assignments_list = len(student_list[int(student_menu_choice) - 1])
                print("The recorded grades for this student are:")
                for i in range(1, assignments_list):
                    print(f"Assignment {i}: {float(student_list[int(student_menu_choice) - 1][i])} %")
                print("Enter 'mean' to get this student's average, enter 'add' to add an assignment's grade to their progile, or enter 'remove' to remove an assignment.\nEnter 'Q' to return to student grade information menu.")
                individual_choice = input("> Enter input: ")
                
                #gets the mean of the student's grades
                if individual_choice.strip().lower() == "mean":
                    student_adder = sum(student_list[int(student_menu_choice) - 1][1:])
                    try:
                        student_average = student_adder / (assignments_list - 1)
                    except ZeroDivisionError:
                        student_average = 0
                    print(border)
                    print(f"The student's average is: {round(student_average, 2)} %.")
                
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