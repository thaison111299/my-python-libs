from __future__ import print_function 
import numpy as np 
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from matplotlib.backends.backend_pdf import PdfPages
import random
np.random.seed(18)

# Tạo dữ liệu bằng cách lấy các điểm theo phân phối chuẩn có kỳ vọng tại (2, 2), (8, 3) và (3, 6),
#  ma trận hiệp phương sai giống nhau và là ma trận đơn vị. Mỗi cụm có 500 điểm. Hiển thị các cụm điểm trên đồ thị.
means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)

X = np.concatenate((X0, X1, X2), axis = 0)
K = 3

original_label = np.asarray([0]*N + [1]*N + [2]*N).T

def kmeans_display(X, label, filename = 'data.pdf'):
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    
    with PdfPages(filename) as pdf:       
        kwargs = {"markersize": 5, "alpha": .8, "markeredgecolor": 'k'}
        plt.plot(X0[:, 0], X0[:, 1], 'b^', **kwargs)
        plt.plot(X1[:, 0], X1[:, 1], 'go', **kwargs)
        plt.plot(X2[:, 0], X2[:, 1], 'rs', **kwargs)

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
    # return index of the closest centroid
    return np.argmin(D, axis = 1)

def kmeans_update_centroids(X, labels, K):
    centroids = np.zeros((K, X.shape[1]))
    for k in range(K):
        # collect all points assigned to the k-th cluster 
        Xk = X[labels == k, :]
        # take average
        centroids[k,:] = np.mean(Xk, axis = 0)
    return centroids

def has_converged(centroids, new_centroids):
    # return True if two sets of centroids as the same
    return (set([tuple(a) for a in centroids]) == set([tuple(a) for a in new_centroids]))



# Phần chính của K-means Clustering.
def kmeans(X, K):
    centroids = [kmeans_init_centroids(X, K)]
    labels = []
    it = 0 
    while True:
        labels.append(kmeans_assign_labels(X, centroids[-1]))
        new_centroids = kmeans_update_centroids(X, labels[-1], K)
        if has_converged(centroids[-1], new_centroids):
        	break
        centroids.append(new_centroids)
        it += 1
    return (centroids, labels, it)







(centroids, labels, it) = kmeans(X, K)
print('Centers found by our algorithm:\n', centroids[-1])



def kmeans_display_centroids(X, label, filename = 'data.pdf'):
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    
    with PdfPages(filename) as pdf:       
        kwargs = {"markersize": 5, "alpha": .8, "markeredgecolor": 'k'}
        plt.plot(X0[:, 0], X0[:, 1], 'b^', **kwargs)
        plt.plot(X1[:, 0], X1[:, 1], 'go', **kwargs)
        plt.plot(X2[:, 0], X2[:, 1], 'rs', **kwargs)

        # draw centroids 
        points = centroids[it]
        kwargs = {"markersize": 15, "markeredgecolor": 'r'}
        animlist = plt.plot(points[0, 0], points[0, 1], 'y^', **kwargs)
        animlist = plt.plot(points[1, 0], points[1, 1], 'yo', **kwargs)
        animlist = plt.plot(points[2, 0], points[2, 1], 'ys', **kwargs)
        #end draw centroids 

        plt.axis([-3, 14, -2, 10])
        plt.axis('scaled')
        plt.plot()
        pdf.savefig(bbox_inches='tight')
        plt.show()



# kmeans_display(X, labels[-1], 'res.pdf')


kmeans_display_centroids(X, labels[-1])
#tham khao: machinelearningcoban.com