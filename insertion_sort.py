def insertion_sort_desc(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Test the function
array = [5, 3, 8, 6, 2]
print("Original Array:", array)
insertion_sort_desc(array)
print("Sorted Array in Decreasing Order:", array)
