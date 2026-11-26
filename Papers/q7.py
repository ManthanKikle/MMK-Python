n = int(input())

def sum_of_digits(n):
    result = 0
    if n <10:
        return n
    else:
        result = n % 10
        return(result + sum_of_digits(n//10))

print(sum_of_digits(n))
