import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose a pivot element (middle of the array)
    left = [x for x in arr if x < pivot]  # Elements smaller than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    return quicksort(left) + middle + quicksort(right)

def generate_random_numbers(n):
    random_numbers = [random.randint(1, 100) for _ in range(n)]
    return random_numbers

random_numbers = generate_random_numbers(50)
print(quicksort(random_numbers))