def is_palindrome(num):
    # Convert number to string and compare with its reverse
    return str(num) == str(num)[::-1]
# Test cases

if is_palindrome(int(input("Enter a number: "))):
    print(" is a Palindrome")
else:
    print( "is Not a Palindrome")
