#so cot ma tran 1 phai = so hang ma tran 2

#vd  a x = x b
import numpy as np
a = np.array([[1,2],
            [3, 4],
            [5, 6] ])
b =np.array([[1, 0],
            [0, 1]
           ])
#ma tran don vi nen la ma tran vuong, the moi make sense


#
#ma tran x ma tran don vi cung kich co = chinh no
# aI = a,
# Ia = a
print(a.dot(b)) ; 


# print(a.transpose()  )
# a = a.transpose() #chuyen vi ma tran 


# c = a.dot(b)

# print(c);


