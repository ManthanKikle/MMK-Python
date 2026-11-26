for rows in range(1,4):
    for cols in range(3 - rows):
        print(" ", end='')
    print(rows, end='')
    for i in range(2*rows -3):
        print("*", end='')
    if rows > 1:
        print(rows, end='')
    print()