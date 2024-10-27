def insertion_sort_descending(arr):
    """Sorts the given array in decreasing order using Insertion Sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        # Shift elements greater than 'key' to the right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place 'key' in its correct position
        arr[j + 1] = key

def display_array(arr, message):
    """Prints the array with a custom message."""
    print(f"{message}: {arr}")
if __name__ == "__main__":
    array = [5, 3, 8, 6, 2]
    display_array(array, "Original Array")
    insertion_sort_descending(array)
    display_array(array, "Sorted Array in Decreasing Order")
    # Example: Add more test cases
    array = [9, 4, 7, 3, 2, 1]
    display_array(array, "New Test Case - Original")
    insertion_sort_descending(array)
    display_array(array, "New Test Case - Sorted")
