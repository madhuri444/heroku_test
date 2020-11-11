import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv(r'C:\Users\madhuri\Desktop\kaggle_datasets\Fish1.csv')
#print(data.head())
#print(data.isna().sum())
x = data.iloc[:,:-1].values
y = data.iloc[:,-1].values

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
Y = le.fit_transform(y)
#print(y,Y)
dict1 ={}
list1 = []
for i,j in zip(y,Y):
    if i not in list1:
        list1.append(i)
        dict1.update({j:i})
#print(dict1)
from sklearn.tree import DecisionTreeClassifier
decision = DecisionTreeClassifier(criterion = "gini",random_state = 42,max_depth = 12)
mod = decision.fit(x,Y)
pickle.dump(decision,open("pickle.pkl","wb"))
model = pickle.load(open("pickle.pkl","rb"))
#out = model.predict([[160,20.5,22.5,25.3,7.0334,3.8203]])
#p = int(out)
def func():
    dict1 = {}
    list1 = []
    for i, j in zip(y, Y):
        if i not in list1:
            list1.append(i)
            dict1.update({j: i})
    return dict1
    # print(dict1)