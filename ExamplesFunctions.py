#Compute the series: 1/1! + 4/2! + 27/3! + …....

def factorial(num):
    fact =1
    for i in range(1, num+1):
        fact *= i
    return fact

num = 3
#num = int(input())
sumSeries = 0
for i in range(1,num+1):
    sumSeries += (i**i/factorial(i))

print(sumSeries)

#Write a function that takes a list of numbers as input and returns the sum of even numbers and the sum of odd numbers separatly:

#n = list(map(int, input().replace(',',' ').split()))
n= [1,2,3,4,5]
odd = 0
even =0
def check(n):
    global odd, even
    if n % 2 ==0:
        even += n
    else:
        odd += n
    return even, odd

for i in n:
    check(i)

print(even)
print(odd)

#Create a function that takes a list as input and returns a new list with the elements reversed. Do not use the built-in reverse() method.

#n = list(map(int,input().replace(',','').split()))

def reverse(lst):
    result = []
    for i in range(len(lst)-1,-1,-1):
        result.append(lst[i])
    return result

print(reverse([1,2,3,4,5]))


#Write a function that takes a list of numbers as input and returns the maximum number in the list

#n= list(map(int, input().replace(',',' ').split()))

def max(lst):
    maximum = lst[0]
    for i in lst:
        if i> maximum:
            maximum = i
    return maximum

print(max([1,2,3,4,5,6]))


#Calculating avegrage grade and The letter of grade

def avg_grade(lst):
    total = 0
    for i in lst:
        total += i
    avg = total/len(lst)
    return avg


def letter_grade(avg):
    if avg > 90:
        print('A')
    elif avg > 80:
        print('B')
    elif avg > 70:
        print('C')
    elif avg > 60:
        print('D')
    else:
        print('F')

avg = avg_grade([55,66,67,89,90])
print(avg)

letter_grade(avg)

#Camel case string

sentence = "tHis Is a StrIng"
words = sentence.split()
def camel_case(words):
    result =''
    for i in words:
        result += i[0].upper() + i[1:].lower()

    print(result)

camel_case(words)

#Common elements in two sets

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

def common(set1,set2):
    result = []
    for i in set1:
        if i in set2:
            result.append(i)
    result = set(result)    
    return result

print(common(set1,set2))


#Swapping two tuple

tup1 = (1,2,3)
tup2 = ('a','b','c')

def swapping(tup1,tup2):
    lst = []
    for i in range(len(tup1)):
        tup1[i],tup2[i] = tup2[i], tup1[i]
    return tup1,tup2

t1 = list(tup1)
t2 = list(tup2)

print(swapping(t1,t2))