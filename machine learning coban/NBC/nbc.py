from __future__ import print_function
from sklearn.naive_bayes import MultinomialNB
import numpy as np
# train data
d1 = [2, 1, 1, 0, 0, 0, 0, 0, 0]
d2 = [1, 1, 0, 1, 1, 0, 0, 0, 0]
d3 = [0, 1, 0, 0, 1, 1, 0, 0, 0]
d4 = [0, 1, 0, 0, 0, 0, 1, 1, 1]


train_data = np.array([d1, d2, d3, d4])
label = np.array(['B', 'B', 'B', 'N'])
V = 9
total_b = []
for i in range(len(d1)):
    total_b.append(d1[i] + d2[i] + d3[i]) 
print(total_b)
NB = sum(total_b)
# print(sum(total_b))
landa_b = [(total_b[i]+1)/(NB + V)  for i in range(len(total_b)) ]


total_n =  d4
NN = sum(total_n)
landa_n = [(total_n[i]+1)/(NN + V)  for i in range(len(total_b)) ]

# print(landa_a)

test = [0, 1, 0, 1, 0, 0, 0, 1, 1] 
test_B_percent = 3/4

for i in range(len(d1)):
    test_B_percent *= landa_b[i]**test[i]

 


# test_B_percent = test_B_percent += total_b[i]**test[i]    for i in range(len(d1)) 

test_N_percent  =  1/4 

for i in range(len(d1)):
    test_N_percent *= landa_n[i]**test[i]

# print(test_N_percent)

test_B_percent  = test_B_percent/(test_B_percent+test_N_percent) 
print(test_B_percent)

# # test data
# d5 = np.array([[2, 0, 0, 1, 0, 0, 0, 1, 0]])
# d6 = np.array([[0, 1, 0, 0, 0, 0, 0, 1, 1]])
# d7 = np.array([[1, 1, 2, 3, 0, 0, 0, 1, 1]])
# ## call MultinomialNB
# model = MultinomialNB()
# # training
# model.fit(train_data, label)
# # test
# print('Predicting class of d5:', str(model.predict(d5)[0]))
# print('Probability of d6 in each class:', model.predict_proba(d7))