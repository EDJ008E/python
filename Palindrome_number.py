a = int(input("Enter a number: "))
def isp(a):
    s = str(a)
    return s == s[::-1]
if isp(a):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")
    
