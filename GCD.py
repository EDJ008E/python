def computeGCD(x, y):
    while (y):
        x, y = y, x % y
    return abs(x)

a = 60
b = 48

print("The GCD of", a, "and", b, "is:", end=" ")
print(computeGCD(a, b))


