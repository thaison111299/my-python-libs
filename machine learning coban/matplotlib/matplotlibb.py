from __future__ import division, print_function, unicode_literals

from matplotlib import rc
import math
import numpy as np 
import matplotlib.pyplot as plt


a = []
b = []
# for i in range(0.0, 11.0, 0.1):
#     a.append(i)
#     b.append(np.sin(i))
i=-5
while i<5:
    a.append(i)
    b.append(  i**2 + 5*np.sin(i)  )
    
    i+= 0.01





x = np.linspace(0, 10, 100) 

plt.plot(a, b, label='linear')  # Plot some data on the (implicit) axes.

# plt.plot(x, x**2, label='quadratic')  # etc.
# plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()