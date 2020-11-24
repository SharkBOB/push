# Train/Test
import numpy
import matplotlib.pyplot as plt
from scipy import stats
import pandas
from sklearn import linear_model
from sklearn.metrics import r2_score

numpy.random.seed(2)
x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(15, 1, 100) / x

Train_x = x[:80]
Train_y = y[:80]

Test_x = x[80:]
Test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(Train_x, Train_y, 4))
myline = numpy.linspace(0, 6, 100)
plt.scatter(Train_x, Train_y)
plt.plot(myline, mymodel(myline))
plt.show()

r2 = r2_score(Train_y, mymodel(Train_x))

print('R2 =', r2)
print(mymodel(5))

# Decision Tree
import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("newtree.csv")
print(df)
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 0, 'NO': 1}
df['Go'] = df['Go'].map(d)

features = ['Age', 'Experience', 'Rank', 'Nationality']
x = df[features]
y = df['Go']

dtree = DecisionTreeClassifier()
dtree = dtree.fit(x, y)
print(dtree.predict([[4, 1, 26, 1]]))

print("[1] means go [2] means not go")

# There are many ways to split the samples, we use the GINI method in this tutorial.
# The Gini method uses this formula:
# Gini = 1 - (x/n)2 - (y/n)2
