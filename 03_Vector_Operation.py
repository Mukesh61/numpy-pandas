''' A 2D array can be defined in the below format '''
import numpy as np

S_X = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8]])

print(S_X)
#[[1 2 3 4]
# [5 6 7 8]]


S_Y = np.array([[9, 8, 6, 3],
               [3, 1, 4, 2]])

print(S_Y)
# [[9 8 6 3]
# [3 1 4 2]]

''' Below some 2D operation has been mentioned '''
print(S_X*S_Y)
#[[ 9 16 18 12]
# [15  6 28 16]]


print(S_X + S_Y)
#[[10 10  9  7]
# [ 8  7 11 10]]


print(S_X % S_Y)
#[[1 2 3 1]
# [2 0 3 0]]

print(S_X * 2)
'''[[ 2  4  6  8]
 [10 12 14 16]]'''

print(S_X/2)
'''[[0.5 1.  1.5 2. ]
 [2.5 3.  3.5 4. ]]'''

print(S_X<2)
'''[[ True False False False]
 [False False False False]]'''
 
 #compare using numpy function 

second_matrix = np.ones((2, 4)) * 2

print(np.less(S_X, second_matrix))
'''[[ True False False False]
 [False False False False]]''' 
