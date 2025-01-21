#largest element in an array
arr = [1000,500,400,30,40,90,20000]
a = arr[0]
for element in arr[1:]:
    if element > a:
        a = element
print("The largest element in the array is:", a)

