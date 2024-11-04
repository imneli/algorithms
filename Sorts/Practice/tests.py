def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quickSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr[n // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)

arr = [7,2,1,3,5,62,2]

def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def merge_sort(arr):
     
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sort = merge_sort(left)
    right_sort = merge_sort(right)

    return merge(left_sort, right_sort)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right): # mescla as duas listas, comparando os elementos e colocando na ordem certa
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result


print(selectionSort(arr))