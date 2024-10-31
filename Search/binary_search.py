def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [11, 12, 22, 25, 34, 64, 90]
x = 25
result = binary_search(arr, x)
print("Binary Search: Elemento encontrado no índice" if result != -1 else "Elemento não encontrado", result)
