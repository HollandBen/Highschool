#Ben Holland
#28 Feb 2024
#Student grades program

#to do:
    #class average function

#important variables
border = "----------------------------------------"
student_list = [
    ["Alex", 98, 99, 97, 100],
    ["Brett", 64, 73, 50, 0],
    ["Edith", 40, 65, 39, 57],
    ["Caden", 85, 89, 78, 91],
    ["Danielle", 90, 92, 91, 99]
]
student_list_length = len(student_list)

#main menu function
def main_menu():
    while True:
        print(border)
        print("Main Menu\nEnter 'mean' to receive the class mean or enter 'students' to access grade information. To make changes to the class list, enter 'edit'.")
        call_main_menu = input("> Enter input: ").lower().strip()
        if call_main_menu == "mean":
            
            #this part is the final(?) part i hope
            #needs to get the sum of the averages of each student, then finds the average between that
            
            
            #below is raw code from the student average getter
            class_adder = sum(student_list[int(student_menu_choice) - 1][1:])
            class_average = student_adder / (assignments_list - 1)
            print(f"The student's average is: '{round(student_average, 2)}%'.")

        elif call_main_menu == "edit":
            edit_student()
        elif call_main_menu == "students":
            student_menu()
        else:
            print("An unexpected value was received. Please try again.")
            
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
    #this loop makes sure that the name is a string, and not a number
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
        elif edit_student_choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")

def student_menu():
    while True:
        global student_average, student_list
        print("Class list:")
        for i in range(0, student_list_length):
            print(i + 1, student_list[i][0])
        print("Enter the student's number to access their profile.\nEnter 'Q' to return to the main menu.")
        student_menu_choice = input("> Enter input: ")
        if student_menu_choice.isdigit() and int(student_menu_choice) <= student_list_length and int(student_menu_choice) >= 1:
            while True:
                print(border)
                print(f"Student selected: {student_list[int(student_menu_choice) - 1][0]}")
                assignments_list = len(student_list[int(student_menu_choice) - 1])
                print("The recorded grades for this student are:")
                for i in range(1, assignments_list):
                    print(f"Assignment {i}: {student_list[int(student_menu_choice) - 1][i]} %")
                print("Enter 'mean' to get this student's average, enter 'add' to add an assignment's grade to their progile, or enter 'remove' to remove an assignment.\nEnter 'Q' to return to student grade information menu.")
                individual_choice = input("> Enter input: ")
                if individual_choice.strip().lower() == "mean":
                    student_adder = sum(student_list[int(student_menu_choice) - 1][1:])
                    student_average = student_adder / (assignments_list - 1)
                    print(f"The student's average is: '{round(student_average, 2)} %'.")
                elif individual_choice.strip().lower() == "add":
                    print("Enter the new percentage grade to be added.")
                    new_grade = input("> Enter input: ")
                    student_list[int(student_menu_choice) - 1].append(round(float(new_grade), 2))
                elif individual_choice.strip().lower() == "remove":
                    print("Enter the assignment number to be removed.")
                    delete_grade = input("> Enter input: ")
                    if int(delete_grade) >= 1 and int(delete_grade) < assignments_list:
                        print(f"Grade '{student_list[int(student_menu_choice) - 1][int(delete_grade)]}' was removed")
                        del student_list[int(student_menu_choice) - 1][int(delete_grade)]
                    else:
                        print("Invalid choice. Please try again.")
                elif individual_choice.strip().lower() == "q":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif student_menu_choice == "q":
            break
        else:
            print("Invalid choice. Please try again.")
            
while True:
    main_menu()