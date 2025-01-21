from datetime import date
birthyear = int(input("Enter your birth year : "))
birthmonth = int(input("Enter your birth month : "))
birthday = int(input("Enter your birth day: "))
currentdate = date.today()
age = currentdate.year - birthyear
if currentdate.month < birthmonth :
    age -= 1
print("Your age is:", age)
