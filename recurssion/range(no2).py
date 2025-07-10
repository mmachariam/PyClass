start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# count while using while loop
while end >= start:
    print(end)
    if start == end:
        break
    end = end -1