"""
Just remember it's called array, not list(which can keep hetrogeneous data)

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

numpy_array.ndim   # 1
numpy_array.shape  # (6,)
numpy_array.size   # 6
numpy_array.dtype  # int64


python_list = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
numpy_array = np.array(python_list)
print(numpy_array)

numpy_array.ndim   # 2
numpy_array.shape  # (2, 6)
numpy_array.size   # 12
numpy_array.dtype  # int64

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

# Indexing & slicing arrays ie. numpy_array[start:stop:step_size], in 2D array numpy_array[start:stop:step_size,start:stop:step_size]
numpy_array[0]  #first element
numpy_array[-1] #last element

# Arithmatic operation
numpy_array + 2
numpy_array * 3

#Filter condition
numpy_array[(other_array == 454) | (other_array < 80)]  # or condition
numpy_array[(other_array == 454) & (other_array < 80)]  # and condition

#where like case statement in sql
np.where(logical_test_condition, this value if true, otherwise this value if false)

np.where(numpy_array <0, "negative number", "positive number")

# Aggregation 
numpy_array.sum()
numpy_array.max()
numpy_array.mean()
numpy_array.min()

numpy_array.sum(axis=0) #aggregates across rows, like add row 0 of column 0 + row 0 of column 1 like this
numpy_array.sum(axis=1) #aggregates across column, like add all column value in a row. 

#Array functions
np.median(numpy_array)
np.percentile(numpy_array)
np.unique(numpy_array)
np.sqrt(numpy_array)




