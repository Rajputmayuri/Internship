class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        return count == 2


my_object = Solution()
print(my_object.isPrime(25))
print(my_object.isPrime(7))
