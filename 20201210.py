# Deep Learning
import pandas as pd
import numpy as np

df = pd.read_excel('customer.xlsx')
# print(df)
X = df.loc[:, ['CreditScore',
               'Geography',
               'Gender',
               'Age',
               'Tenure',
               'Balance',
               'NumOfProducts',
               'HasCrCard',
               'IsActiveMember',
               'EstimatedSalary']]

y = df.Exited
print(y.head())

# Process categorical data convert to numerical values
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

lablecoder1 = LabelEncoder()
lablecoder2 = LabelEncoder()
X.Geography = lablecoder1.fit_transform(X.Geography)
X.Gender = lablecoder2.fit_transform(X.Gender)
print(X.head())

onehotencoder = OneHotEncoder(categories='auto')
X = onehotencoder.fit_transform(X).toarray()
# delete the Interfering terms
X = np.delete(X,[0],1)
print(X[0])

# Row vectors to column vectors.
y = y[:,np.newaxis]
onehotencoder = OneHotEncoder()
y=onehotencoder.fit_transform(y).toarray()
print(y)

# Create test and train set

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
print(len(X_train))
print(len(X_test))

# Standardize the data
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.fit_transform(X_test)

# decision tree
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))
