from __future__ import print_function 
import numpy as np 
import gzip
# from sklearn.datasets import fetch_mldata
# mnist = fetch_mldata('MNIST original', data_home='../../data/')
# from sklearn.datasets import fetch_openml

# fetch_openml

with gzip.open("Desktop\\mnist\\t10k-images-idx3-ubyte.gz", "rb") as f:
    mnist = f.read()
N = 200
X = mnist[np.random.choice(mnist.shape[0], N)]/255.