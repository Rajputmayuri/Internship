def upperBound(arr, x):
    n = len(arr)
    ub = n
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > x:
            ub = mid
            high = mid - 1
        else:
            low = mid + 1

    return ub


print(upperBound([1, 3, 4, 6, 7, 9, 10, 11], 5))
