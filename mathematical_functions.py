import math
from math import pi

#Square root: .sqrt
sqrt_result = math.sqrt(25)
print(sqrt_result)

#Exponential : .pow
pow_result = math.pow(2,3)
print(pow_result)

#Trigonometric Functions(in radians): .sin(), .cos(), .tan()
sin_result = math.sin(pi/4)
cos_result = math.cos(pi/3)
tan_result = math.tan(pi/6)

print(sin_result)
print(cos_result)
print(tan_result)

#Logarithmic functions .log(), .log10()
logResult = math.log(10, 2)
log10Result = math.log10(100)

print(logResult)
print(log10Result)

#Constants: .pi, .e
pi_value = math.pi
e_value = math.e

print(pi_value)
print(e_value)

#factorial: .factorial()

factorial_value = math.factorial(5)
print(factorial_value)

#absolute value: .fabs()

absolute_value = math.fabs(-pi)
print(absolute_value)

#Ceil: .ceil()

ceil_value = math.ceil(3.6)
print(ceil_value)

#floor: .floor()

floor_value = math.floor(3.6)
print(floor_value)

#Random 

import random
random_float = random.random()
print(random_float)

random_float_range = random.uniform(1.5,3.0)
print(random_float_range)

random_integer = random.randint(1,10)
print(random_integer)

options = ['a','b','c','d']
choice = random.choice(options)
print(choice)

