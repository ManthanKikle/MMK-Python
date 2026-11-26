n = int(input())

for rows in range(1,n+1):
    for cols in range(1,rows+1):
        letters = chr(64 + cols)
        print(f"{letters}{cols}", end=' ')
    print()