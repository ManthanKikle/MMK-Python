#Making Function that returns a value

def add(a,b):
    return a +b

result = add(3,5)
print(result)

#Making Function that prints and greets

def greet(name):
    print(f"Hello, {name}!")

greet("MMK")

#Assigning a function to a variable

def subs(x,y):
    return x -y

a = 6
b= 7
diff = subs
print(diff(a,b))

#Program to print all characters in a string

def allcharstr(istr):
    for i in istr:
        print(i)

#inputstr = input("Enter a String: ")
inputstr = "HIII MMK"
allcharstr(inputstr)

#Function to calculate a factorial of a number

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print(factorial(11))

#Using global Variables

n = 10

def updaten():
    global n
    n += 5

print("Before: ",n)

updaten()

print("After: ", n)

#Function that squares with a explicit return

def sqrt_num(n):
    return n **2

result = sqrt_num(7)
print(result) 