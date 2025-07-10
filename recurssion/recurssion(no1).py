def countdown(n):
    if n < 1:
        return
    print(n)
    countdown(n-1)

n = int(input("Enter a number: "))
countdown(n)

# or
"""
print(n)

    if n ==1:
        return
    else:
        countdown(n-1)
        
countdown(10)
"""