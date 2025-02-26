"""
Numpy Array: 
1. Fixed size
2. Single Data type
3. Array can be modified but size cannot be changed.
4. 1 dimension or multi dimension
"""
import numpy as np

python_list = [1, 2, 3, 4, 5, 6]
numpy_array = np.array(python_list)
print(numpy_array)

print(numpy_array.ndim)  # 1
print(numpy_array.shape) # (6,)
print(numpy_array.size) # 6
print(numpy_array.dtype) # int64


python_list = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
numpy_array = np.array(python_list)
print(numpy_array)

print(numpy_array.ndim) # 2
print(numpy_array.shape) # (2, 6)
print(numpy_array.size) # 12
print(numpy_array.dtype) # int64

np.ones(5,) #array([1., 1., 1., 1., 1.])

np.zeros((3,5), dtype=int)
'''
array([[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0]])
'''

np.arange(15) #array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

np.linspace(0, 200, 5) #array([  0.,  50., 100., 150., 200.])

numpy_array.reshape(1, 12) #array([[ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12]])



