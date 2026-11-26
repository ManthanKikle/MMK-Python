"""
Illustrate the use of NumPy in a
Python program to accept two 2 x 2 matrices from 
the user and perform matrix addition, subtraction,
multiplication, element-wise multiplication, 
and transpose of the first matrix.


""" 
import numpy as np

m1 = np.array(input().split(), dtype=int).reshape(2,2)
m2 = np.array(input().split(), dtype=int).reshape(2,2)

print(m1+m2)
print(m1-m2)
print(m1@m2)
print(m1*m2)
print(m1.T)