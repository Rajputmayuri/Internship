"""Check if two strings are anagrams."""


def anagram():

    s1 = input("Enter a 1st string=").replace(" ", "").lower()
    s2 = input("Enter a 2nd string=").replace(" ", "").lower()

    if sorted(s1) == sorted(s2):
        print("The strings are anagrams")
    else:
        print("The strigns are not anagrams")


anagram()
