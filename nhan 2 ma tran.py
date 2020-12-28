#so cot ma tran 1 phai = so hang ma tran 2

#vd  a x = x b
import numpy as np
a = np.array([[3,4],[5, 6]])
b =np.array([[2,5,7,8],[3,6,9,10]])

# c = a.dot(b)

# print(c);

c = [[1, 2, 3]]
d = [[4,5,6]]
c = np.array(c)
c = c.T
print(c)
print(d)

print(c.dot(d))

