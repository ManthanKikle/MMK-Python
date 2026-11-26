import numpy as np

A = np.array([[3,1,1],
              [1,2,1],
              [1,1,3]])

B = np.array([[11],
              [10],
              [13]])

inv_A = np.linalg.inv(A)

X= inv_A @ B

print(X)

print(f"x ={X[0][0]}")
print(f"y ={X[1][0]}")
print(f"z ={X[2][0]}")