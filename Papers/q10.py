"""
draw the pattern
1
4 4
9 9 9
16 16 16 16
"""

n= int(input())

for i in range(1,n+1):
    for j in range(1, i+1):
        print(i**2, end=' ')
    print()