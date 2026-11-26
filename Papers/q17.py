import numpy as np

seq = [1,5,6,9,7,8,2,4,3,10,12,11]

seq_re = np.array(seq).reshape(3,4)

print("The Original: ",seq)
print("2D :", seq_re)

rowSum = np.sum(seq_re, axis=1)
colSum = np.sum(seq_re, axis=0)

print(rowSum, colSum)

print(seq_re*2)

print(np.unique(seq_re))
