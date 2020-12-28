#so cot ma tran 1 phai = so hang ma tran 2

#vd  a x = x b
import numpy as np
a = np.array([[1,2],
            [3, 4]])


b =np.linalg.pinv(a) #ma tran gia nghich dao cua a, co the coi la ma tran nghich dao cua a, nhan a thanh ma tran don vi 

print(a.dot(b))


# print(1.00000000e+00 - 1)

# b =np.array([[1, 0],
#             [0, 1]
#            ])

# cach tim ma tran nghich dao cua a 

# a-a = i




# print(a.dot(b)) ; 


# print(a.transpose()  )
# a = a.transpose() #chuyen vi ma tran 


# c = a.dot(b)

# print(c);


# Nếu một ma trận có một hàng hoặc một cột là một vector0, thì định thức của nó bằng 0
# .6.Một ma trận là khả nghịch khi và chỉ khi định thức của nó khác 0


