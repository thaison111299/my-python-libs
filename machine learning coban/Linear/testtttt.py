
# for both python 2 and 3 
from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
# x= [[0, 1 , 2 , 3]]
# x = np.array(x)
# w = [[1, 2]]
# w = np.array(w)

# print(np.dot(x.T, w)   )


x = [ [1, 2], [1,3],[1,4],[1,5]] 


x = np.array(x)
print(x)
# print(x.shape )

w = [[1], [2]]

w = np.array(w)

# print(w.shape)

print( np.dot(x, w).shape )
