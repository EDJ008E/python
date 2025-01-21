def bin(n):
    if ( n > 0):
        bin((int)(n/2))
        print(n%2,end ="")
        n = int(input("enter the decimal number:"))
        bin(n)