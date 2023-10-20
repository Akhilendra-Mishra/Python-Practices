import numpy
from numpy import *

m1 = matrix('1 2 3 ; 6 4 5 ; 1 6 7 ')
m2 = matrix('1 2 3 ; 6 8 5 ; 2 6 7 ')

m3 = m1 * m2

print(m3)
print()

#for find the diagonal from matrix....
print(numpy.diagonal(m3))
print()

#which type of data present in matrix...
print(m3.dtype)
print()

#dimantion type of matrix....
print(m3.ndim)
print()

#shape of matrix...
print(m3.shape)
print()

#size of matrix...
print(m3.size)
print()

#reshape of matrix...
arr4 = m3.reshape(3,1,3)
print(arr4)
print()

arr4 = m3.reshape(9,1)
print(arr4)
print()

arr4 = m3.reshape(1,9)
print(arr4)
print()