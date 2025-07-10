def countdown(start, end):
    print(end)

    if start == end:
        return
    else:
        countdown(start, end - 1)

countdown(45, 50)
