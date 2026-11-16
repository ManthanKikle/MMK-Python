import numpy as np

#Creating arrays (np.array, .shape)

a1 = np.array([1,2,3,4,5])
a2 = np.array([[1,2,3],[4,5,6]])

print(a1, a1.shape)
print(a2, a2.shape)

#Addition (+ and add())

a1 = np.array([1,2,3,4])
a2 = np.array([3,4,5,6])

print(np.add(a1,a2))
print(a1 + a2)

#Subtraction (- and subtract())

a1 = np.array([1,2,3,4])
a2 = np.array([3,4,5,6])

print(np.subtract(a2,a1))
print(a1-a2)

#Multiplication (* and multiply())

a1 = np.array([2,3,4,5])
a2 = np.array([6,7,8,9])

print(np.multiply(a1,a2))
print(a1*a2)

#Division (/ and divide())

a1 = np.array([7,8,9,10])
a2 = np.array([3,4,5,6])

print(np.divide(a1,a2))
print(a1/a2)

#Exponentiation

a = np.array([1,2,3,4])

print(np.power(a,3))
print(a ** 3)

#modulus

a = np.array([2,5,6,7,8,9])
print(np.mod(a,2))
print(a % 2)

#Creating 2x2 and 3x3 matrices

print(np.array([[1,2,3],[2,3,4]]))
print(np.array([[2,3,4],[3,4,5],[4,5,6]]))

#Matrix multiplication with np.dot()

a1 = np.array([[1,2],[3,4]])
a2 = np.array([[5,6],[8,9]])

print(np.dot(a1,a2))

#Dot product of different shapes

a1 = np.array([[2,3,4],[1,2,3],[3,4,5]]) # 3x3
a2 = np.array([[3,4],[5,6],[9,1]]) #3x2

print(np.dot(a1,a2)) # 3x3

#Transpose(3 ways)

a = np.array([[1,2],[3,4],[5,6]])
print(np.transpose(a))
print(a.transpose())
print(a.T)

#Trace (sum of the diagonal)

a = np.array([[2,3,4],[1,2,1],[7,8,7]])
print(sum(a.diagonal()))
print(a.trace())
print(np.trace(a))

#Flatten

a = np.arange(1,10).reshape(3,3)
print(a)
print(a.flatten())

#Rank

a = np.array([[1,2,4],[5,6,7],[7,8,8]])
b = np.arange(1,10).reshape(3,3)
print(np.linalg.matrix_rank(a))
print(np.linalg.matrix_rank(b))

#Determinant

a = np.array([[13,42,26],[62,53,44],[5,7,5]])
det = np.linalg.det(a)
print(det)

#Inverse

a = np.array([[4,3,4],[3,6,7],[7,8,8]])
inv = np.linalg.inv(a)
print(inv)

#Slicing rows and columns

a = np.array([[2,5,7],[7,8,9],[4,33,99]])
print(a[:,:2]) # first two columns
print(a[:2,:]) # frist two row
print(a[:,-1]) # last column
print(a[-1,:])

#Create a matrix `A` as follows: A = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]]) Calculate and print the sum of the elements in the first two columns of matrix `A` using NumPy

A = np.array([[2,4,6],[8,10,12],[14,16,18]])

fist_two_col= A[:,:2]

sum = np.sum(fist_two_col)
print(sum)

#Create a matrix `B` as follows: B = np.array([[1, 3], [5, 7], [9, 11]]) Calculate and print the trace of matrix `B` using NumPy.
B = np.array([[1, 3], [5, 7], [9, 11]])
trace_B = np.trace(B)
print(trace_B)

#Create a matrix `C` as follows: C = np.array([[2, 5, 8], [1, 4, 7], [3, 6, 9]]) Calculate and print the sum of the diagonal elements of matrix `C` using loops.

C = np.array([[2, 5, 8], [1, 4, 7], [3, 6, 9]])

diagonal_sum = 0

for i in range(len(C)):
    diagonal_sum += C[i][i]

print(diagonal_sum, np.diagonal(C).sum())

#Create a matrix `D` as follows: D = np.array([[3, 6], [9, 12], [15, 18]]) Calculate and print the sum of the elements in the last column of matrix `D` using NumPy.

D = np.array([[3, 6], [9, 12], [15, 18]])

last_col = D[:,-1]
sumLastCol = np.sum(last_col)
print(sumLastCol)

#Create a matrix `E` as follows: E = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) Calculate and print the product of the diagonal elements of matrix `E` using loops.

E = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

dia_E = np.diagonal(E)
print(dia_E)
product = 1
for i in range(len(dia_E)):
    product *=dia_E[i]

print(product)

#Create a matrix `F` as follows: F = np.array([[2, 4], [6, 8], [10, 12]]) Calculate and print the sum of the elements in the last row of matrix `F` using NumPy

F = np.array([[2, 4], [6, 8], [10, 12]])

lastRow = F[-1,:]
sum = np.sum(lastRow)
print(sum)

#Create a matrix `G` as follows: G = np.array([[1, 2], [3, 4], [5, 6]]) Calculate and print the sum of all elements in matrix `G` using NumPy.

G = np.array([[1, 2], [3, 4], [5, 6]])

sum = np.sum(G)
print(sum)

#Create a matrix `H` as follows: H = np.array([[5, 6, 7], [8, 9, 10], [11, 12, 13]]) Calculate and print the product of the diagonal elements of matrix `H` using loops.

H = np.array([[5, 6, 7], [8, 9, 10], [11, 12, 13]])

diagonalH = np.diagonal(H)
productDiaH = 1 
for i in range(len(diagonalH)):
    productDiaH *= diagonalH[i]

print(productDiaH)

#Create a matrix `I` as follows: I = np.array([[3, 7], [2, 6], [1, 5]]) Calculate and print the trace of matrix `I` using NumPy.

I = np.array([[3, 7], [2, 6], [1, 5]])

traceI = np.trace(I)
print(traceI)

#Create a matrix `J` as follows: J = np.array([[4, 5, 6], [7, 8, 9], [10, 11, 12]]) Calculate and print the sum of the elements above the main diagonal of matrix `J` using loops.

J = np.array([[4, 5, 6], [7, 8, 9], [10, 11, 12]])

rows, cols = J.shape
sum_above_diag = 0

for i in range(rows):
    for j in range(cols):
        if j< i:
            sum_above_diag += J[i][j]

print(sum_above_diag)