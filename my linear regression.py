# for both python 2 and 3 
from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages




def transposeMatrix(a):
    # if len(a)
    # a = [[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]] #no dang giu hang, de thay hang phai co them hang
    # b = list(a)
   
    # print(b)
    b = []

    if len(a)==1:
        for i in a[0]:
            b.append([i])
        # [[147], [150], [153], [158], [163], [165], [168], [170], [173], [175], [178], [180], [183]]
    elif len(a)>1:
        c=  []


        for i in range(len(a[0])):
            c.append(len(a)*[0])
        
        # c=   [   list([0]*10 )  ] 

        for  i in range(    len(a[0])    ):
            for j in range(  len(a)    ):
                c[i][j]  =  a[j][i]
        #         # c[i][j]=1
        #         # print(a[j][i]) 
        #         c[1][2] = a[j][i]
        #         break 
        #     break 
        # c[0][0]  = 1
        # c[0][1] = 2
        # b = c
        
        # for i in c:
        #     for d in i:
        #         print(d)
        b = list (c) 
    return b
    # print(len(a))


def printMatrix(a):
    print('[', end='')
    for i in range(len(a)) :
        # print('[', end='')
        if i == len(a) -1:
            
            print(a[i], end='') 
        else:
            print(a[i])
        # print(']', end='')

    print(']')

def one(d1=1, d2= 1):
    return [[1]]*d1 

def  concatenate(a, b):
    c = []
    n = len(a) #or len(b)
    for i in range(len(a)):
        c.append(  [a[i][0], b[i][0]]  )
    return c  

def dot(a, b ):
    c = []
    for _ in range(len(a)):
        c.append(  [0] *  len(b[0] )  )

    for i in range(len(a)):  
        for j in range(len(b[0])): #j dai dien cho cac cot cua b     
            summ = 0.0
            #process 
            # for k in range(len(a[0]) ):  #k dai dien cho cac phan tu tren tung hang a
            #     summ += a[i][k]* b[j][i]    
            for k in range( len(a[0]) ):
                    summ+= a[i][k] * b[k][j]
            #process
            c[i][j]= summ  
            
    return(c)

# height (cm)
X = [[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]
y = [[49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]

# print(Y)

X = transposeMatrix(X)
# printMatrix(X)

one = one(len(X))

Xbar  = concatenate( one ,X )

# printMatrix (   dot(transposeMatrix(Xbar), Xbar)   ) 




# printMatrix(Xbar)

# printMatrix(transposeMatrix(Xbar))






# transposeMatrix(Xbar)
# print("Z: \n")
# printMatrix(Xbar)

# X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T # each row is a point 

# weight (kg)
# y = np.array([ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68])
# Visualize data 
# plt.plot(X, y, 'ro')
# plt.axis([140, 190, 45, 75])
# plt.xlabel('Height (cm)')
# plt.ylabel('Weight (kg)')
# plt.show()


# Building Xbar 
# one = np.ones((X.shape[0], 1))

# printMatrix(X)

# print(one)
# Xbar = np.concatenate((one, X), axis = 1) # each point is one row 
# # Calculating weights of the fitting line 
# A = np.dot(Xbar.T, Xbar)


A = dot(transposeMatrix(Xbar), Xbar)
# print(b)

b = dot(transposeMatrix(Xbar), transposeMatrix(y))
z  = np.linalg.pinv(A)

# print(type(z))
z.tolist()

w = dot(z, b)
# print(w)


w_0 = w[0][0] 
w_1 = w[1][0]  


y1 = w_1*155 + w_0
y2 = w_1*160 + w_0

print('Input 155cm, true output 52kg, predicted output %.2fkg'  %(y1) )
print('Input 160cm, true output 56kg, predicted output %.2fkg'  %(y2) )




# print(b)
# print(transposeMatrix(Xbar))
# print()


# b = np.dot(Xbar.T, y)
# w = np.dot(np.linalg.pinv(A), b)
# # weights
# w_0 = w[0]
# w_1 = w[1]

# x0 = np.linspace(145, 185, 2, endpoint=True)
# y0 = w_0 + w_1*x0

# # Drawing the fitting line 
# plt.plot(X, y, 'ro')     # data 
# plt.plot(x0, y0)           # the fitting line
# plt.axis([140, 190, 45, 75]) # xmin, xmax, ymin, ymax 
# plt.xlabel('Height (cm)', fontsize = 14)
# plt.ylabel('Weight (kg)', fontsize = 14)
# plt.tick_params(axis='both', which='major', labelsize=14)
# with PdfPages('lr_ex.pdf') as pdf:
#     pdf.savefig(bbox_inches='tight')
# plt.show()



# y1 = w_1*155 + w_0
# y2 = w_1*160 + w_0

# print('Input 155cm, true output 52kg, predicted output %.2fkg'  %(y1) )
# print('Input 160cm, true output 56kg, predicted output %.2fkg'  %(y2) )



