s = input("Enter String to check for Palindrome: ").lower()
if s == s[::-1]:
    print("Palindrome :) ")
else:
    print("Not Palindrome :( ")