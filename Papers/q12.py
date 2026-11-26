"""Read n (0 ≤ n ≤ 10). Define factorial(n) recursively, with 0! = 1, and define permutations(n, r)
to return n!/(n−r)! using factorial() and integer division. Read r (0 ≤ r ≤ n), call the functions and 
display both results.
Example: n = 5, r = 2 -> Factorial: 120; Permutations: 20
"""
def factorial(n):
    if n > 0: 
        return n*factorial(n-1)
    else:
        return 1


    
def permutation(n,r):
    return factorial(n)/factorial(n-r)

print(f"""
factorial: {factorial(5)}
Permutation: {permutation(5,2)}
""")

