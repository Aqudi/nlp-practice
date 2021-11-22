import numpy as np


scala = np.array(5)
print('scala:', scala)
print('scala ndim:', scala.ndim)
print('scala shape:', scala.shape)

vector = np.array([1, 2, 3, 4])
print('\nvector:', vector)
print('vector ndim:', vector.ndim)
print('vector shape:', vector.shape)

matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('\nmatrix:', matrix)
print('matrix ndim:', matrix.ndim)
print('matrix shape:', matrix.shape)

tensor = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]],
])
print('\ntensor:', tensor)
print('tensor ndim:', tensor.ndim)
print('tensor shape:', tensor.shape)
