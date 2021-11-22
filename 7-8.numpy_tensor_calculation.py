import numpy as np


# 벡터의 덧셈, 뺄셈
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)
print(a-b)

# 행렬의 덧셈, 뺄셈
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])
print(a+b)
print(a-b)

# 벡터의 내적
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.dot(a, b))

# 행렬의 곱셈
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])
print(np.matmul(a, b))
