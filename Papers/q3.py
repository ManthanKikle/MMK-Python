"""
the workstation never stores the raw 3×3 signal matrix; instead, it first applies
a linear transformation to it using matrix multiplication. Later, to retrieve the original signal, the
system must reverse this transformation. The signal matrix itself is to be generated at runtime using
random integers between 1 and 9. Write a Python program using NumPy that generates the signal
matrix, applies the given transformation, reconstructs the original matrix using an appropriate
numerical operation on T, and confirms that the reconstruction is correct.
"""
import numpy as np

t = np.array([[4,1,2],
              [0,3,1],
              [2,1,5]])

r = np.random.randint(1,10, size = (3,3))
b = t @ r

s = np.linalg.inv(t) @ b

print(t)
print(r)
print(s)