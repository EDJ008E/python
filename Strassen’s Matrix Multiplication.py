# define the matrices
x = [[0,2],[0,1]]
print("matrix x is:")
for i in range(len(x)):
     print("\t",x[i])

y = [[0,0],[3,4]]
print("matrix y is:")
for i in range(len(y)):
     print("\t",y[i])

# define the Strassen function
def st(a, b):
    s = [
        b[0][1]-b[1][1],a[0][0]+a[0][1],
        a[1][0]+a[1][1],b[1][0]-b[0][0],
        a[0][0]+a[1][1],b[0][0]+b[1][1],
        a[0][1]-a[1][1],b[1][0]+b[1][1],
        a[0][0]-a[1][0],b[0][0]+b[0][1]
    ]
    p = [
        a[0][0]*s[0],s[1]*b[1][1],
        s[2]*b[0][0],a[1][1]*s[3],
        s[4]*s[5],s[6]*s[7],s[8]*s[9]
    ]
    c = [
        [p[4]+p[3]-p[1]+p[5],p[0]+p[1]],
        [p[2]+p[3],p[4]+p[0]-p[2]-p[6]]
    ]
    return c

# print the result
result = st(x, y)
print("Strassen's matrix multiplication result is")
for row in result:
    print(row)
