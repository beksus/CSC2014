import numpy as np

# Change all the elements in the first column of array2D_int to 2014. Save your Python script file as lab2_ex2.py.

# Example initialization of array2D_int
array2D_int = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# Change all elements in the first column to 2014
array2D_int[:, 0] = 2014

# Print to verify
print(array2D_int)