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


"""Analyze the execution of nested for loops by developing a Python program to generate pairs of numbers (m, n) as follows:
i) The outer for loop should iterate m from 1 to 4.
ii) For each value of m, the inner for loop should iterate n from 1 to 5.
iii) If n == 3, skip the current iteration of the inner loop using continue.
iv) If m == 3, terminate the current execution of the inner loop using break.
v) Print each pair (m, n) that satisfies these conditions.

Explain the purpose of the break and continue statements in your program."""

for m in range(1,5):
    for n in range(1,6):
        if n== 3:
            continue
        if m==3:
            break

        print(f"({m},{n})")