from __future__ import print_function 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from matplotlib.backends.backend_pdf import PdfPages
import random
np.random.seed(18)  


# name = []

# Xs = {}
# for i in range(3):
#     name.append("X" + str(i))

# for na in name:
#     Xs[na] = 32131;

# print(Xs)

temp = tuple()
Xs = {"dsadas":2, "eewq":3}
for key in Xs:
    # print(Xs[key])
    temp+= (Xs[key],)
    # temp.__add__(Xs[key])
print(temp)