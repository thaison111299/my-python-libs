import pandas as pd 
dataframe = pd.read_csv('Advertising.csv')
x = dataframe.values[:, 4]
# print(x)

print('{', end='')
for i in x:
    print(i, end=',')  
print('}', end='')