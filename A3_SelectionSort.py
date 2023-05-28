def selection_sort(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_index = i
        
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


def main():
    # Get user input for the list of numbers
    numbers = input("Enter a list of numbers, separated by spaces: ").split()
    
    # Convert the input strings to integers
    numbers = [int(num) for num in numbers]
    
    # Call the selection sort function
    sorted_numbers = selection_sort(numbers)
    
    # Print the sorted list
    print("Sorted list:", sorted_numbers)


if __name__ == "__main__":
    main()
