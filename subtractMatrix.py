import numpy
from numpy import *

m1 = matrix('1 2 3; 6 4 5; 1 6 7')
m2 = matrix('1 2 3; 6 8 5; 2 6 7')

m3 = m2-m1

print(m3)

print(numpy.diagonal(m3))
