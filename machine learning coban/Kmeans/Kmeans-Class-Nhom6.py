from __future__ import print_function 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from matplotlib.backends.backend_pdf import PdfPages
import random
# from voronoi import voronoi_finite_polygons_2d



np.random.seed(18)


N = 56
X = np.array([[0, 1], [0, 2], [0, 3], [0, 4], [0, 6], [0, 7], [0, 8], [0, 9],
[1, 1], [1, 2], [1, 3], [1, 4], [1, 6], [1, 7], [1, 8], [1, 9], [2, 1], 
[2, 2], [2, 3], [2, 4], [2, 6], [2, 7], [2, 8], [2, 9], [3, 1], [3, 2],
[3, 3], [3, 4], [3, 6], [3, 7], [3, 8], [3, 9], [4, 1], [4, 2], [4, 3],
[4, 4], [4, 6], [4, 7], [4, 8], [4, 9], [5, 1], [5, 2], [5, 3], [5, 4],
[5, 6], [5, 7], [5, 8], [5, 9], [6, 1], [6, 2], [6, 3], [6, 4], [6, 6],
[6, 7], [6, 8], [6, 9]])



K = 2
original_label = np.asarray([0]*28 + [1]*28).T

def kmeans_display(X, label, filename = 'data.pdf'):
    X0 = X[label == 0, :] 
    X1 = X[label == 1, :]
    
    with PdfPages(filename) as pdf:       
        kwargs = {"markersize": 5, "alpha": .8, "markeredgecolor": 'k'}
        plt.plot(X0[:, 0], X0[:, 1], 'b^', **kwargs)
        plt.plot(X1[:, 0], X1[:, 1], 'go', **kwargs)



        plt.axis([-3, 14, -2, 10])
        plt.axis('scaled')
        plt.plot()
        pdf.savefig(bbox_inches='tight')
        plt.show()
    
kmeans_display(X, original_label)


def kmeans_init_centroids(X, k):
    # randomly pick k rows of X ans initial centroids
    return X[np.random.choice(X.shape[0], k)]

def kmeans_assign_labels(X, centroids):
    # calculate pairwise distances btw data and centroids
    D = cdist(X, centroids)
    return np.argmin(D, axis = 1)    #phan tu nao nho nhat tren hang D

def kmeans_update_centroids(X, labels, K):
    centroids = np.zeros((   K, X.shape[1]    ) )   #tao 1 mang  3 x 2 voi gia tri 0

    for k in range(K):
        # collect all points assigned to the k-th cluster 
        Xk = X[labels == k, :] #lay cai X nao ma thuoc hang co gia tri bang k va lay het, Xk la 1 list 
        # take average
        centroids[k,:] = np.mean(Xk, axis = 0) #cach viet nay  = centroids[k][:]
    return centroids

def has_converged(centroids, new_centroids):
    return  ( [ tuple (a) for a in centroids]   ==  [tuple (b)for b in new_centroids])


def kmeans(X, K):
    centroids = [kmeans_init_centroids(X, K)]
    labels = []
    it = 0 
    while True:
        labels.append(  kmeans_assign_labels(X,  centroids[-1] ) )  #kmeans_assign_labels tra ve  np.argmin(D, axis = 1) 
        new_centroids = kmeans_update_centroids(X, labels[-1], K)
        if has_converged(centroids[-1], new_centroids):
        	break
        centroids.append(new_centroids)
        it += 1
    
    return (centroids, labels, it)




(centroids, labels, it) = kmeans(X, K)


# print('label: \n', labels[-1].shape  )

print('Centers found by our algorithm:\n', centroids[-1])






def kmeans_display_centroids(X, label, filename = 'data.pdf'):
    X0 = X[label == 0, :] 
    X1 = X[label == 1, :]
    
    with PdfPages(filename) as pdf:       
        kwargs = {"markersize": 5, "alpha": .8, "markeredgecolor": 'k'}
        plt.plot(X0[:, 0], X0[:, 1], 'b^', **kwargs)
        plt.plot(X1[:, 0], X1[:, 1], 'go', **kwargs)

        #draw centroids
        points = centroids[it]
        kwargs = {"markersize": 15, "markeredgecolor": 'k'}
        animlist = plt.plot(points[0, 0], points[0, 1], 'y^', **kwargs)
        animlist = plt.plot(points[1, 0], points[1, 1], 'yo', **kwargs)
        # animlist = plt.plot(points[2, 0], points[2, 1], 'ys', **kwargs)

        plt.axis([-3, 14, -2, 10])
        plt.axis('scaled')
        plt.plot()
        pdf.savefig(bbox_inches='tight')
        plt.show()


kmeans_display_centroids(X, labels[-1], 'res.pdf')



while True:
    
    row = int(input('row find: '))

    column = int(input('column find: '))
    if row == -1 or column == -1:
        print ('ket thuc')
        break
    print('bạn ở dãy số: {0}'.format ( kmeans_assign_labels(np.array([[row, column]]) , centroids[-1]) + 1)     )





