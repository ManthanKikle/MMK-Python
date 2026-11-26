import numpy as np

n = np.arange(20)

matrix = n.reshape(4,5)
print(matrix)

print(matrix[1:])
print(matrix[:,2])

matrix[matrix % 2 ==0] = -1

print(matrix)