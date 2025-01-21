number = int(input("Enter a number: "))
isprime = True

if number <= 1:
    isprime = False
elif number <= 3:
    isprime = True
elif number % 2 == 0 or number % 3 == 0:
    isprime = False
else:
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            isprime = False
            break
        i += 6

if isprime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")



