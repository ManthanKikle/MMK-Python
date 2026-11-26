#Lambda module

add = lambda x,y: x + y
print(add(5,3))

square = lambda x: x**2
print(square)

#SYS
import sys
print("\n PythonPath = \n", sys.path)

#Math
from math import pi, sqrt
print(sqrt(16))
print(pi)

#Calendar

import calendar
print(calendar.month(2025,4))

#dir
def print_var(x):
    print(x)

print_var(10)
print(dir())