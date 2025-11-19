
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]             # The element we want to insert
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than 'key'
        # one position ahead to make room for 'key'
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key        # Insert key into its correct position
    
    return arr
