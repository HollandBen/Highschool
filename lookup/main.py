#Ben Holland
#20 March 2024
#Seaching and sorting assignment

#important variables
names_list = [
    "Andy", "Bill", "Cherry", "William", "Nancy", "Bob", "Smith", "Dan", "Gabby", "Sam", 
    "Xander", "Billy", "Tommy", "Lilith", "Hyacinthe"
    ]
border = "----------------------------------------\n"

#Below are the given searching / sorting algorithms

# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index
def selection_sort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])

def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
    
def main():
    while True:
        print(border)
        print("Please enter 'search' to enter the search bar, or enter 'add' or 'remove' to edit the list of terms.\nEnter 'Q' to quit the program.")

#activates the program
main()