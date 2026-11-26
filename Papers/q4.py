"""
Draw the following pattern:
1
1 # 2
1 # 2 # 3
1 # 2 # 3 # 4
"""

n= int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
        if j<i:
            print("#", end='')

    print()