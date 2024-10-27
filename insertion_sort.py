def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def display_array(arr, message):
    print(f"{message}: {arr}")

if __name__ == "__main__":
    array = [5, 3, 8, 6, 2]
    display_array(array, "Original Array")
    insertion_sort_descending(array)
    display_array(array, "Sorted Array in Decreasing Order")
