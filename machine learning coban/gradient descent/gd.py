
from __future__ import print_function 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from matplotlib.backends.backend_pdf import PdfPages
import random
from sklearn.linear_model import LinearRegression 


X = np.random.rand(1000)
y = 4 + 3 * X + .5*np.random.randn(1000) # noise added

# Building Xbar 
one = np.ones( (X.shape[0],1) )
Xbar = np.concatenate((one, X.reshape(-1, 1)), axis = 1)

def grad(w):
    N = Xbar.shape[0]
    return 1/N * Xbar.T.dot(Xbar.dot(w) - y)

def cost(w):
    N = Xbar.shape[0]
    return .5/N*np.linalg.norm(y - Xbar.dot(w))**2


def myGD(grad, w_init, eta):
    w = [w_init]
    for it in range(100):
        w_new = w[-1] - eta*grad(w[-1])
        if np.linalg.norm(grad(w_new))/len(w_new) < 1e-3: #tai sao phai chia cho len?
            break 
        w.append(w_new)
    return (w, it)

w_init = np.array([2, 1])
(w1, it1) = myGD(grad, w_init, 0.1)
print('Sol found by GD: w = ', w1[-1], ',\nafter %d iterations.' %(it1+1))