# Matrix Algebra

# All Code copy/pasted from ../jupyter

#1.1 Matrix A is 2x3
#1.2 Matrix B is 2x2
#1.3 Matrix C is 3x2
#1.4 Matrix D is 2x3
#1.4 Vector u is 1x4
#1.5 Vector w is 4x1

#----------------------------------------------------------#

# 2.1
import numpy as np
u = np.asarray([6,2,-3,5])
v = np.asarray([3,5,-1,4])

calc = u + v
by_hand =  [(6+3),(2+5), (-3+-1), (5+4)]

print("calculated: {0} by_hand: {1}".format(calc,by_hand))

#2.2
import numpy as np
u = np.asarray([6,2,-3,5])
v = np.asarray([3,5,-1,4])

calc = np.subtract(u,v) 
by_hand = [(6-3), (2-5), (-3--1), (5-4)]

print("calculated: {0} by_hand: {1}".format(calc,by_hand))

#2.3
import numpy as np
a = 6
u = np.asarray([6,2,-3,5])

calc = np.multiply(a,u) 
by_hand = [(6*6), (6*2), (6*-3), (6*5)]

print("calculated: {0} by_hand: {1}".format(calc,by_hand))

#2.4
import numpy as np
u = np.asarray([6,2,-3,5])
v = np.asarray([3,5,-1,4])

calc = np.dot(u,v) 
by_hand = (6*3) + (2*5) + (-3*-1) + (5*4)

print("calculated: {0} by_hand: {1}".format(calc,by_hand))

#2.5
import math
from numpy import linalg as LA
u = np.asarray([6,2,-3,5])

calc = LA.norm(u)

mag = lambda x : math.sqrt(sum(i**2 for i in x))
by_hand= mag(u)

print("calculated: {0} by_hand: {1}".format(calc,by_hand)) 

#----------------------------------------------------------#

#3.1
import numpy as np
A = np.asarray([[1,2,3],[2,7,4]])     # 2x3
C = np.asarray([[5,-1],[9,1],[6,0]])  # 3x2

# NOTE Not going to work as  addition/subtraction require matrices of the same dimensions

#3.2
import numpy as np
A = np.asarray([[1,2,3],[2,7,4]])
C = np.asarray([[5,-1],[9,1],[6,0]])

calc = A-C.transpose() 
by_hand = [ [(1-5), (2-9), (3-6)], [(2--1), (7-1), (4-0)]]


print("calc: \n{0} \nby_hand: \n{1}".format(calc,by_hand)) 


#3.3
import numpy as np
C = np.asarray([[5,-1],[9,1],[6,0]])
D = np.asarray([[3,-2,-1],[1,2,3]])

calc = C.transpose() + 3*D
# by hand done in in notebook: https://www.dropbox.com/s/p6qqifksa4zckcn/Metis-Linear-Algebra-3-3.jpg?dl=0

print(calc)


#3.4
import numpy as np
B = np.asarray([[1,-1],[0,1]])    # 2x2
A = np.asarray([[1,2,3],[2,7,4]]) # 2x3
calc = np.dot(B,A)
print(calc)
# by hand done in in notebook: https://www.dropbox.com/s/uv4qx6ht2bso3u6/File%20Jun%2010%2C%2012%2044%2041%20PM.jpeg?dl=0


#3.5
import numpy as np
B = np.asarray([[1,-1],[0,1]])
A = np.asarray([[1,2,3],[2,4,7]])
calc = np.dot(B,A.transpose())

# Shapes are wrong. Won't work: Columns count in B need to be the same as row count in A.transpose







