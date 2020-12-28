
# for both python 2 and 3 
from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages


# height (cm)
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T # each row is a point 
# weight (kg)
y = np.array([ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68])
# Visualize data 
plt.plot(X, y, 'ro')
plt.axis([140, 190, 45, 75])
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
# plt.show()


# Building Xbar 
one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1) # each point is one row  

print(Xbar)
print(Xbar.shape)
# ct w0x  + w1X  = y 

# print(Xbar)
# # Calculating weights of the fitting line 
A = np.dot(Xbar.T, Xbar)  #XTX 
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)   #day la ham gia nghich dao => chung ta tim thang nghiem cua phuong trinh voi moi diem luon 

# print(w)    

# weights
w_0 = w[0]
w_1 = w[1]

x0 = np.linspace(145, 185, 2, endpoint=True)  
y0 = w_0 + w_1*x0

# Drawing the fitting line 
plt.plot(X, y, 'ro')     # data 
plt.plot(x0, y0)           # the fitting line
plt.axis([140, 190, 45, 75]) # xmin, xmax, ymin, ymax 
plt.xlabel('Height (cm)', fontsize = 14)
plt.ylabel('Weight (kg)', fontsize = 14)
plt.tick_params(axis='both', which='major', labelsize=14)
with PdfPages('lr_ex.pdf') as pdf:
    pdf.savefig(bbox_inches='tight')
plt.show()



y1 = w_1*155 + w_0
y2 = w_1*160 + w_0

print('Input 155cm, true output 52kg, predicted output %.2fkg'  %(y1) )
print('Input 160cm, true output 56kg, predicted output %.2fkg'  %(y2) )