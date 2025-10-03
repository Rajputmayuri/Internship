"""1st method using sort function"""

arr = [1, 3, 5, 90, 45, 23, 65]
arr.sort()
print(arr[-2])

"""Time Complexity : O(NlogN)
   Space Complexity : O(1)"""

"""2nd method"""

arr = [1, 3, 5, 90, 45, 23, 65]
largest = float("-inf")
second_largest = float("-inf")
n = len(arr)
for i in range(0, n):
    if arr[i] > largest:
        largest = arr[i]
for i in range(0, n):
    if arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]
print(second_largest)

"""Time Complexity : O(N)
   Space Complexity : O(1)"""

"""3rd method"""
arr = [1, 3, 5, 90, 45, 23, 65]
largest = float("-inf")
s_largest = float("-inf")
n = len(arr)
for i in range(0, n):
    if arr[i] > largest:
        s_largest = largest
        largest = arr[i]
    elif arr[i] > s_largest and arr[i] != largest:
        s_largest = arr[i]
print(s_largest)

"""Time Complexity : O(N)
   Space Complexity : O(1)"""
