n = 5  # Number of rows in one half

# Upper part of the pattern
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# Lower part of the pattern
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
