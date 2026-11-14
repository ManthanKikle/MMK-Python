#Create t = (10, 20, 30, 40, 50). Print the first element, the last element, the slice t[1:4], and the reversed tuple.
t = (10, 20, 30, 40, 50)

print(t)
print(t[0])
print(t[-1])
print(t[1:4])
print(t[::-1])

#Print all elements of a tuple using a for loop.

t = (10, 20, 30, 40, 50)

for i in t:
    print(i)

#Find the sum and average of all numbers in a tuple (3, 7, 9, 12).

t = (3, 7, 9, 12)

sum = 0
for i in t:
    sum += i

avr = sum/len(t)
print(f"Sum is: {sum}, Avrage is: {avr}")

#Find the largest and smallest numbers in a tuple without using max() or min()

t = (1,2,3,4,5,6,7)
largest = t[0]
smallest = t[0]
for i in t:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i


print(f"The Smallest is: {smallest} and The largest is: {largest}")

#Print only the even numbers from (1, 2, 3, 4, 5, 6, 7, 8)

t = (1, 2, 3, 4, 5, 6, 7, 8)
even = []
odd = []
for i in t:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)

#Count how many numbers in (10, 25, 30, 45, 5, 60) are greater than a value entered by the user.

t = (10, 25, 30, 45, 5, 60)
n = 9
count = 0
for i in t:
    if i > n:
        count += 1

print(f"The count is: {count}")

#Create a new tuple containing the squares of each number in (2, 4, 6, 8)

t = (2, 4, 6, 8)
squares = []

for i in t:
    squares.append(i**2)

squares = tuple(squares)

print(squares)

#Reverse a tuple using a loop (don’t use slicing).

t = (2,4,56,7,8,9,99)
r=[]

for i in range(len(t)-1, -1,-1):
    r.append(t[i])

r = tuple(r)
print(r)


#Combine two tuples element-wise: (1, 2, 3) and (4, 5, 6)

t1 = (1,2,3)
t2 = (4,5,6)

combined_tuple = []

for i in range(len(t1)):
    combined_tuple.append(t1[i] + t2[i])

combined_tuple = tuple(combined_tuple)

print(combined_tuple)

#Separate the even and odd numbers of (10, 15, 22, 33, 40, 55) into two tuples.

t = (10, 15, 22, 33, 40, 55)

odd =[]
even = []

for i in t:
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

odd = tuple(odd)
even = tuple(even)

print(f"Even: {even}, Odd: {odd}")

#Check whether a number is prime by storing its factors in a tuple

t = 10
if t <=1:
    print(n,"Not prime")
else:
    factors = []
    for i in range(1, n+1):
        if t % i ==0:
            factors.append(i)
    if len(factors) == 2:
        print(t, "Is a Prime number")
    else:
        print(t,"not a prime Number")

factors = tuple(factors)
print(factors)

