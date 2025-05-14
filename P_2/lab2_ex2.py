import numpy as np


array2D_int = np.array([[1,2,3],[4,5,6],[7,8,9]])

array2D_int[:, 0] = 2014

print(array2D_int)


import numpy as np

# Original 4x4 array
array_4x4 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# New row to insert (as a 1x4 array)
new_row = np.array([[2, 0, 1, 4]])

# Insert the new row after the second row (index 2)
array_5x4 = np.concatenate(
    (array_4x4[:2], new_row, array_4x4[2:]), axis=0
)

print(array_5x4)