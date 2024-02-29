#Ben Holland
#28 Feb 2024
#Student grades program

#important variables
border = "----------------------------------------"
student_list = [
    ["Alex", 98, 99, 97, 100],
    ["Brett", 64, 73, 50, 0],
    ["Caden", 85, 89, 78, 91],
    ["Danielle", 90, 92, 91, 99]
]


#come back to the below later

student_list_length = len(student_list)
#for i in range(student_list_length):
class_mean = student_list[0][1:]
#class_mean = class_mean / student_list_length
#print(round(class_mean, 2))

#student_list.append([new_student_name])
        #while True:
            #student_list[-1].extend([int((input("Enter a percentage grade: ")))])

#main menu function
def main_menu():
    while True:
        print(border)
        print("Main Menu\nEnter 'mean' to receive the class mean or enter a student's number or name to access grade information. To make changes to the class list, enter 'edit'.")
        call_main_menu = input("Enter input: ").lower().strip()
        if call_main_menu == "mean":
            print(f"The mean of the class is: {class_mean} %")
        elif call_main_menu == "edit":
            edit_student()
        elif call_main_menu == student_list[0]:
            student_menu()
        elif call_main_menu.isdigit():
            student_menu()
        else:
            print("An unexpected value was received. Please try again.")
            
#editing the student list function
def edit_student():
    print(border)
    print("Enter 'add' to add a student to the list or enter 'remove' to remove a student from the list.\nPress 'Q' to return to the main menu.")
    while True:
        edit_student_choice = input("Enter input: ")
    #this loop makes sure that the name is a string, and not a number
        if edit_student_choice == "add":
            while True:
                new_student_name = input("Enter the new student's name: ")
                if new_student_name.isdigit():
                    print("Invalid name. Please try again.")
                else:
                    new_student_name.strip().capitalize()
                    student_list.append([new_student_name])
                    break
        elif edit_student_choice == "remove":
            print("Enter the student's number to remove them from the list.")
            while True:
                remove_student = input("Enter input: ")
                if remove_student.isinstance(str):
                    print("Invalid student number. Please try again.")
                else:
                    int(remove_student)
                    #continue from here tomorrow :)
        elif edit_student_choice == "q":
            #something here
        else:
            print("Invalid choice. Please try again.")
                
            
    
new_student()
print(student_list)