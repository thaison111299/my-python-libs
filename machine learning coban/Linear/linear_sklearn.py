from sklearn import datasets, linear_model
import numpy as np 
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt


# fit the model by Linear Regression
regr = linear_model.LinearRegression()


X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([ 49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])


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
regr.fit(X, y) # in scikit-learn, each sample is one row
# Compare two results
print("scikit-learn’s solution : w_1 = ", regr.coef_[0], "w_0 = ", regr.intercept_)
print("our solution : w_1 = ", w[1], "w_0 = ", w[0])


