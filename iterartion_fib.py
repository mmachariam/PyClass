n = int(input("Enter the number of terms: "))

a, b = 0, 1  # First two terms of the series

print("Fibonacci Series:")

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b