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
student_list_length = len(student_list)
for i in range(student_list):
    class_mean = student_list[0][1:]
print(class_mean)

#main menu function
def main_menu():
    print(border)
    print("Main Menu\nEnter 'mean' to receive the class mean or enter a student's number or name to access grade information. To add a new student, enter 'new'.")
    call_main_menu = input("Enter input: ").lower().strip()
    if call_main_menu == "mean":
        print(f"The mean of the class is: {class_mean} %")
    elif call_main_menu == "new":
        new_student()
    elif call_main_menu == student_list[0]:
        student_menu()
    elif call_main_menu.isdigit():
        student_menu()
    else:
        print("An unexpected value was received. Please try again.")
        
