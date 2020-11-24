import numpy
import matplotlib.pyplot as plt
from scipy import stats
import pandas
from sklearn import linear_model

# x=numpy.random.uniform(0.0,5.0,1000000)
# plt.hist(x,100)
# plt.show()

# y=numpy.random.normal(5.0,1.0,100000)
# plt.hist(y,100)
# plt.show()

x = [2, 3, 5, 6, 8, 9, 10, 15]
y = [12, 32, 65, 78, 113, 245, 665, 999]
plt.scatter(x, y)
plt.show()
slope, intercept, rvalue, pvalue, stderr = stats.linregress(x, y)


def myfunc(x):
    return slope * x, +intercept


mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

df = pandas.read_excel('car.csv')
print(df)
x = df[['Weight', 'Volume']]
y = df[['CO2']]
print(x)
print(y)

# Use the linear model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

scaledX = scale.fit_transform(x)

regr = linear_model.LinearRegression()
regr.fit(scaledX, y)

scaled = scale.transform([[2300, 1.3]])
print(scaled)
PreictedCO2 = regr.predict([scaled[0]])
print(PreictedCO2)

# Predict the CO2 EMISSION of a car where the weight is 2300 kg, and the VOLUME IS 1300CM3
'''
PredictCO2=regr.predict([[2300,1300]])
print(PredictCO2)
print(regr.coef_)

'''
# You do not have to do this manually,
# the Python sklearn module has a method called StandardScaler()
# which returns a Scaler object with methods for transforming data sets.

# The standardization method uses this formula:
# z = (x - u) / s
# Where z is the new value, x is the original value, u is the mean and s is the standard deviation.


