import numpy as np

a = np.array([[1, 2, 3], [4,5,6]])
b = np.array([[4, 5, 6],[5,6,7]])


result = float(np.dot(a, b.T))

print(result)