from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
from matplotlib.backends.backend_pdf import PdfPages
import random

np.random.seed(18)

# K = int(input("Nhập số K: ").strip())
# if K > 100:
#     K = 100
#     print("Vì K  lớn hơn 100 nên đặt k thành 100 nha, vì có ít màu và biểu tượng quá! Sorry!")
K = 100
means = []

c = 1
v = 1

for i in range(K):
    means.append([c%8, v%8])
    if c == 8:
        v+=2
    c+=2

cov = [[1, 0], [0, 1]] 
N=400

Xnum = {}
for i in range(K): 
    Xnum['X'+ str(i)] = np.random.multivariate_normal(means[i], cov, N)

temp  = tuple()

for key in Xnum:
    temp += (Xnum[key],)


X = np.concatenate(   temp  , axis=0)

temp  = []
for i in range(K):
    temp += [i]*N

original_label = np.array(temp).T


def kmeans_display(X, label, filename='data.pdf'):
    with PdfPages(filename) as pdf:
        kwargs = {"markersize": 5, "alpha": .8, "markeredgecolor": 'k'}
    
        colors = ['b', 'g', 'r', 'y', 'm', 'c', 'k']
        markers = ['o', 'v', '^', '<', '>', '8', 's', 'h','D','P', 'p']
        c, v = 0, 0
        for i in range(K):
            plt.plot((X[label == i, :])[:, 0],(X[label== i, :])[:, 1],  colors[c%len(colors)] + markers[v%len(markers)] , **kwargs)
            c+= 1
            v+= 1
        plt.axis([-3, 14, -2, 10])
        plt.axis('scaled')
        plt.plot()
        pdf.savefig(bbox_inches='tight')
        plt.show()


# kmeans_display(X, original_label)
print("Processing...")

def kmeans_init_centroids(X, k):
    # randomly pick k rows of X ans initial centroids
    return X[np.random.choice(X.shape[0], k)]


def kmeans_assign_labels(X, centroids):
    # calculate pairwise distances btw data and centroids
    D = cdist(X, centroids)
    # return index of the closest centroid
    # print(len(D), len(D[0]))

    return np.argmin(D, axis=1)  # phan tu nao nho nhat tren hang D


def kmeans_update_centroids(X, labels, K):
    centroids = np.zeros((K, X.shape[1]))  # tao 1 mang  3 x 2 voi gia tri 0

    for k in range(K):
        # collect all points assigned to the k-th cluster
        # lay cai X nao ma thuoc hang co gia tri bang k va lay het, Xk la 1 list
        Xk = X[labels == k, :]
        # take average
        # cach viet nay  = centroids[k][:]
        centroids[k, :] = np.mean(Xk, axis=0)

    return centroids


def has_converged(centroids, new_centroids):
    # return True if two sets of centroids as the same
    # print("centroids: ", centroids)
    # print("new_centroids: ", new_centroids)
    return ([tuple(a) for a in centroids] == [tuple(b)for b in new_centroids])

    # vay tai sao phai dung ham set???


def kmeans(X, K):
    centroids = [kmeans_init_centroids(X, K)]
    labels = []
    it = 0
    while True:
        # kmeans_assign_labels tra ve  np.argmin(D, axis = 1)
        labels.append(kmeans_assign_labels(X,  centroids[-1]))
        new_centroids = kmeans_update_centroids(X, labels[-1], K)
        if has_converged(centroids[-1], new_centroids):
            break
        centroids.append(new_centroids)
        it += 1

    return (centroids, labels, it)


#######
(centroids, labels, it) = kmeans(X, K)

print("CENTROIDS FINDED: \n", centroids[-1])


# print('label: \n', labels[-1].shape  )

# print('Centers found by our algorithm:\n', centroids[-1])



def kmeans_display_centroids(X, label, filename='data.pdf'):
    with PdfPages(filename) as pdf:
        kwargs = {"markersize": 5, "alpha": .8, "markeredgecolor": 'k'}
    
        colors = ['b', 'g', 'r', 'y', 'm', 'c', 'k']
        markers = ['o', 'v', '^', '<', '>', '8', 's', 'h','D','P', 'p']
        c, v = 0, 0
        for i in range(K):
            plt.plot((X[label == i, :])[:, 0],(X[label== i, :])[:, 1],  colors[c%len(colors)] + markers[v%len(markers)] , **kwargs)
            c+= 1
            v+= 1

        # draw centroids 
        points = centroids[it]
        kwargs = {"markersize": 15, "markeredgecolor": 'r'}
        v=0
        for i in range(K):
            animlist = plt.plot(points[i, 0], points[i, 1], 'y' + markers[v%len(markers)], **kwargs)
            # animlist = plt.plot(points[1, 0], points[1, 1], 'yo', **kwargs)
            # animlist = plt.plot(points[2, 0], points[2, 1], 'ys', **kwargs)
            v+=1
        # draw centroids 


        plt.axis([-3, 14, -2, 10])
        plt.axis('scaled')
        plt.plot()
        pdf.savefig(bbox_inches='tight')
        plt.show()





kmeans_display_centroids(X, labels[-1], 'res.pdf')
#####


# return ve 1 mang co 3 x 3, gia tri cac phan tu = 0
# print(np.zeros( (3, 3) )) pr np.zeros([3,3])

# print(X.shape)
# print(np.zeros((3, 2)))
