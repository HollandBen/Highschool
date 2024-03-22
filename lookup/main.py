#Ben Holland
#20 March 2024
#Seaching and sorting assignment

#important variables
terms = ["Andy", "Bill", "Cherry", "William", "Nancy", "Bob", "Smith", "Dan", "Gabby", "Sam", 
    "Xander", "Billy", "Tommy", "Lilith", "Hyacinthe"]
border = "----------------------------------------\n"
length = len(terms)

#Below are the given searching / sorting algorithms

# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def selection_sort(terms, length):
    
    for ind in range(length):
        min_index = ind
 
        for j in range(ind + 1, length):
            # select the minimum element in every iteration
            if terms[j] < terms[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (terms[ind], terms[min_index]) = (terms[min_index], terms[ind])

def binary_search(terms, low, high, wanted):
    
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if terms[mid] == wanted:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif terms[mid] > wanted:
            return binary_search(terms, low, mid - 1, wanted)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(terms, mid + 1, high, wanted)
 
    else:
        # Element is not present in the array
        return -1
    
def main():
    while True:
        print(border)
        print("Please enter 'search' to enter the search bar, or enter 'add' or 'remove' to edit the list of terms. Enter 'Q' to quit the program.")
        call_main = input("> Enter input: ").lower().strip()
        if call_main == "search":
            search()
        elif call_main == "add":
            add()
        elif call_main == "remove":
            remove()
        elif call_main == "q":
            break
        else:
            print("Invalid input. Please try again.")

#searching the list function and automatically sorts
def search():
    global terms, length
    length = len(terms)
    while True:
        print(border)
        print("Please enter the search term (case sensitive). Enter 'Q' to return to the main menu.")
        call_search = input("> Enter input: ")
        if call_search.strip().lower() == "q":
            break
        else:
            selection_sort(terms, length)
            search_result = binary_search(terms, 0, length - 1, call_search)
            if search_result == -1:
                print(f"Term '{call_search}' was not found in the list.")
            else:
                print(f"Term '{terms[search_result]}' was found in slot #{search_result + 1}.")

#adding a new term to the list function
def add():
    global terms
    while True:
        print(border)
        print("Please enter the new term to be added to the list. Enter 'Q' to return to the main menu.")
        call_add = input("> Enter input: ")
        if call_add.strip().lower() == "q":
            break
        else:
            terms.append(call_add)
            print(f"New term '{call_add}' has been added.")

#removing a term from the list function
def remove():
    global terms
    while True:
        print(border)
        show_terms()
        print("Please enter the value of the term to be removed from the list. Enter 'Q' to return to the main menu.")
        call_remove = input("> Enter input: ").strip()
        if call_remove.lower() == "q":
            break
        elif call_remove.isdecimal and int(call_remove) > 0 and int(call_remove) <= length:
            print(f"Term '{terms[int(call_remove) - 1]}' was removed.")
            terms.pop(int(call_remove) - 1)
        else:
            print("Invalid input. Please try again.")
            
#short function to show the sorted terms
def show_terms():
    global length
    length = len(terms)
    selection_sort(terms, length)
    print("Term list:")
    for i in range(length):
        print(i + 1, terms[i])
        
        
#activates the program
main()