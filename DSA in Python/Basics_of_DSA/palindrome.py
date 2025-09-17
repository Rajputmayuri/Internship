class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        palindrome_number = 0
        while num > 0:
            last_digit = num % 10
            palindrome_number = (palindrome_number * 10) + last_digit
            num //= 10
        return palindrome_number == x


obj = Solution()
print(obj.isPalindrome(121))
print(obj.isPalindrome(123))
