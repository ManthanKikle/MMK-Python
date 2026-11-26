

def sum_digits(num):
    if num == 0:
        return 0
    result = num % 10
    num = num//10
    return result + sum_digits(num)

print(sum_digits(574))