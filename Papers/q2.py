"""
Write a python program using nested for-loops to generate an N x N square grid pattern based on
the following rules:
(1) Place stars * at all four corners of the square grid.
(2) Create a smaller sub-square inside the grid that spans from row 2 to row (n - 1) and column 2
"""
n = int(input())
for rows in range(1,n+1):
    for cols in range(1,n+1):

        if (rows == 1 or rows == n) and (cols == 1 or cols== n ):
            print(" * ", end='')
        elif rows >= 2 and rows <= n -1 and cols >=2 and cols <= n-1:
            if rows == 2 or rows == n-1 or cols == 2 or cols == n-1:
                print(" * ", end='')
            else:
                print("   ", end= '')
        else:
            print("   ", end='')

    print()


        