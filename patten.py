n = 5
for i in range(1, n + 1):
    # print("".join(str(j) for j in range(*[i, n + 1])))



    print(" " * (n - i - 1) + "*" * (1 * i + 1))
