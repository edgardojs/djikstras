def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Found the target, return its index
        elif arr[mid] <= target:  # Adjusted condition
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target is not in the array

array = [5, 7, 8, 9, 10]  # Sorted array
target = 8
print(array)

result = binary_search(array, target)
if result != -1:
    print(f"Element {target} is found at index {result}.")
else:
    print(f"Element {target} is not in the array.")