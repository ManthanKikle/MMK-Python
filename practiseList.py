#Print all elements of a list

numbers = [1,3,5,6,7]

print(numbers)

#Sum all numbers in a list

numbers = [2,5,6,8,7]

total = 0

for n in numbers:
    total += n

print(total)

#Find the largest number 

numbers = [3,5,6,75,440]

largest = numbers[0]
for n in numbers:
    if n > largest:
        largest = n

print(largest)


#Find the even number from the list

numbers = [4,56,78,9,80,43]

even = numbers[0]

for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')

print()

#Create a new list with square of each number

numbers = [3,4,5,7,9]

squares = []
for i in numbers:
    squares.append(i ** 2)

print(squares)

#Count how many numbers are greater than a given value

n = 9
numbers = [2,4,6,44,56]
count = 0

for i in numbers:
    if i > n:
        count += 1

print(count)

#reverse a list using a loop

num = [1,2,3,4,5,6]
reverse_num = []
List_num = len(num) 

for i in range(List_num-1, -1, -1):
    reverse_num.append(num[i])

print(reverse_num)

#combine two lists element-wise

list1 = [1,4,6]
list2 = [2,3,7]

sum_list =[]

for i in range(len(list1)):
    sum_list.append(list1[i]+list2[i])

print(sum_list)


#separate even and odd numbers into two lists

numbers = [2,3,45,8,9,21, 66]
even_list = []
odd_list = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        even_list.append(numbers[i])
    else:
        odd_list.append(numbers[i])

print(f"Even:{even_list}, Odd: {odd_list}")

#Check if a Number is Prime or Not:
n = int(input())
if n <= 1:
    print(n, "not a prime number")
else:
    factor = []
    for i in range(1, n+1):
        if n % i ==0:
            factor.append(i)
    if len(factor) == 2:
        print(n,"is Prime")
    else:
        print(n,"is Not Prime")