
# Stock tree
import pandas as pd
import numpy as np

df = pd.read_excel('Stock.xlsx')
X = df.drop('rise',axis=1)
y = df.rise
# print(X.shape)
# print(y.shape)

# process the categorical data convert to numerical values

'''
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict

d = defaultdict(LabelEncoder)
X_trans = X.apply(lambda x: d[x.name].fit_transform(x))

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
print(X_train.shape)
print(X_test.shape)

from sklearn import tree
clf = tree.DecisionTreeClassifier(max_depth=3)
clf = clf.fit(X_train,y_train)

# Review the result

test_rec = X_test.iloc[1]
print(test_rec)
print(clf.predict(X_test.iloc[1]))

'''