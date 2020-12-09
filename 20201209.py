# Loans Tree
import pandas as pd

df = pd.read_excel('locans.xlsx')
X = df.drop('safe_loans', axis=1)
y = df.safe_loans
# print(X.shape)
# print(y.shape)

# process the categorical data convert to numerical values

from sklearn.preprocessing import LabelEncoder
from collections import defaultdict

d = defaultdict(LabelEncoder)
X_trans = X.apply(lambda x: d[x.name].fit_transform(x))
# print(X_trans.head())

# Split the data randomly into training data and test data


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_trans, y, random_state=1)
print(X_train.shape)
print(X_test.shape)

# Build the decision tree
from sklearn import tree

clf = tree.DecisionTreeClassifier(max_depth=3)
clf = clf.fit(X_train, y_train)

# Review the result

# test_rec = X_test.iloc[1]
# print(test_rec)
print(clf.predict(X_test))

from  sklearn.metrics import accuracy_score
print(accuracy_score(y_test,clf.predict(X_test)))



