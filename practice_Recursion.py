#Factorial using recursion

def fact(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

print(fact(10))

#Calculate Exponent x^y

def expo(x,y):
    if y==0:
        return 1
    else:
        return x*expo(x, y-1)

print(expo(10,2))

#Print the fibbonachi series 
 
def fibbo(n):
    if n <=1:
        return n
    else:
        return (fibbo(n-1)+fibbo(n-2))

for i in range(10):
    print(fibbo(i))


#Grestest Common Divisor

def gcd(a,b):
    if b>a:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a %b)

print(gcd(48,18))

#Sum till n natural numbers

def sum(n):
    if n == 0 :
        return 0
    else:
        return n+ sum(n-1)

print(sum(2))

