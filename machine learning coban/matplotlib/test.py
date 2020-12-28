from __future__ import division, print_function, unicode_literals

from matplotlib import rc
import math
import numpy as np 
import matplotlib.pyplot as plt
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
#rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)



def grad(x):
    return 2*x+ 5*np.cos(x)

def cost(x):
    return x**2 + 5*np.sin(x)



x = -5
for i in range(100):
    
    x = x - 0.5*grad(x)
    print(grad(x))  
    if abs(grad( x )) < 1e-3:
        print('hoi tu: ',x)
        break

print('Cost = ', cost(x))   
print('iter = ', i)  


# print('1e-3',1e-3)