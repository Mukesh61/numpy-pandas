'''
Universal functions(ufunc)

A universal function is a function that operates on ndarrays in an element by element fashion, supporting array broadcasting, type casting and several other standard features. that is ufunc is a "vectorized"
wrapper for a function that takes a fixed number of specific inputs and produces a fixed number of specific outputs.
'''

import pandas as pd

s = pd.Series(ranges(10))
s.max()

max(s)

'''
pandas function is faster because of vectorized. 
'''
