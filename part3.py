def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    return sum(int(digit) ** power for digit in num_str) == n

num = int(input("Enter a number: "))
print(f"{num} is an Armstrong Number" if is_armstrong(num) else f"{num} is Not an Armstrong Number")
