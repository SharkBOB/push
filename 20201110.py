# Sorting Arrays
# Sorting means putting elements in an ordered sequence.
#
# Ordered sequence is any sequence that has an order corresponding to elements,
# Like numeric or alphabetical, ascending or descending.
#
# The NumPy ndarray object has a function called sort(), that will sort a specified array.
#
# Example
# Sort the array:

import numpy as np

arr = np.array([3, 2, 0, 1, 60, 50, 1, 70])
arr = np.sort(arr)
print(np.sort(arr))

filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
newarr = arr[filter_arr]
print(newarr)

# What are ufuncs?
# ufuncs stands for "Universal Functions" and they are NumPy functions that operates on the ndarray object.
#
# Why use ufuncs?
# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
#
# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.
#
# ufuncs also take additional arguments, like:
#
# where boolean array or condition defining where the operations should take place.
#
# dtype defining the return type of elements.
#
# out output array where the return value should be copied.
#
# What is Vectorization?
# Converting iterative statements into a vector based operation is called vectorization.
#
# It is faster as modern CPUs are optimized for such operations.
#
# Add the Elements of Two Lists
# list 1: [1, 2, 3, 4]
#
# list 2: [4, 5, 6, 7]
#
# One way of doing it is to iterate over both of the lists and then sum each elements.

list1 = [1, 2, 3, 4]
list2 = [2, 3, 5, 6]
z = []
for i, j in zip(list1, list2):
    z.append(i + j)
print(z)
# Json
import json

# someJSON
x = '{"name":"JHON","AGE":30,"CITY":"NEW YORK"}'

# parse x
# the result is the Python dictionary
y = json.loads(x)
print(y["AGE"])

x = {"name": "mike", "age": 20}
y = json.dumps(x)
# the result is the JSON STRING
print(y)

# Seaborn
# Visualize Distributions With Seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs.
# It will be used to visualize random distributions.

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([1, 2, 5, 6, 7])
plt.show()

# Normal (Gaussian) Distribution
# The Normal Distribution is one of the most important distributions.
#
# It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.
#
# It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
#
# Use the random.normal() method to get a Normal Data Distribution.
#
# It has three parameters:
#
# loc - (Mean) where the peak of the bell exists.
#
# scale - (Standard Deviation) how flat the graph distribution should be.
#
# size - The shape of the returned array.

from numpy import random

x = random.normal(size=(2, 3))
x = random.normal(loc=1, scale=2, size=(2, 3))
sns.distplot(random.normal(size=1000), hist=False)
print(x)
plt.show()

# Binomial Distribution
# Binomial Distribution is a Discrete Distribution.
#
# It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
#
# It has three parameters:
#
# n - number of trials.
#
# p - probability of occurence of each trial (e.g. for toss of a coin 0.5 each).
#
# size - The shape of the returned array.

sns.distplot(random.binomial(n=10, p=0.5, size=10000), hist=True, kde=False)
plt.show()

# Difference Between Normal and Poisson Distribution
# Normal distribution is continous whereas poisson is discrete.
#
# But we can see that similar to binomial for a large enough poisson distribution
# It will become similar to normal distribution with certain std dev and mean.

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='possion')

plt.show()

# Difference Between Poisson and Binomial Distribution
# The difference is very subtle it is that, binomial distribution is for discrete trials,
# whereas poisson distribution is for continuous trials.
#
# But for very large n and near-zero p binomial distribution is near identical to poisson distribution
# such that n * p is nearly equal to lam.

sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()

# Uniform Distribution
# Used to describe probability where every event has equal chances of occuring.
#
# E.g. Generation of random numbers.
#
# It has three parameters:
#
# a - lower bound - default 0 .0.
#
# b - upper bound - default 1.0.
#
# size - The shape of the returned array.

x = random.uniform(size=(2, 3))
print(x)
sns.distplot(random.uniform(size=1000), hist=False)
plt.show()

# Logistic Distribution
# Logistic Distribution is used to describe growth.
#
# Used extensively in machine learning in logistic regression, neural networks etc.
#
# It has three parameters:
#
# loc - mean, where the peak is. Default 0.
#
# scale - standard deviation, the flatness of distribution. Default 1.
#
# size - The shape of the returned array.

x = random.logistic(loc=1, scale=2, size=(2, 3))

# sns.distplot(random.logistic(size=1000),hist=False)

# Difference Between Logistic and Normal Distribution
# Both distributions are near identical,
# but logistic distribution has more area under the tails.
# ie. It representage more possibility of occurence of an events further away from mean.
#
# For higher value of scale (standard deviation)
# the normal and logistic distributions are near identical apart from the peak.

sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show()

# Multinomial Distribution
# Multinomial distribution is a generalization of binomial distribution.
#
# It describes outcomes of multi-nomial scenarios unlike binomial
# where scenarios must be only one of two. e.g. Blood type of a population, dice roll outcome.
#
# It has three parameters:
#
# n - number of possible outcomes (e.g. 6 for dice roll).
#
# pvals - list of probabilties of outcomes (e.g. [1/6, 1/6, 1/6, 1/6, 1/6, 1/6] for dice roll).
#
# size - The shape of the returned array.

x = random.multinomial(n=6, pvals=[1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6])
print(x)

# Exponential Distribution
# Exponential distribution is used for describing time till next event e.g. failure/success etc.
#
# It has two parameters:
#
# scale - inverse of rate ( see lam in poisson distribution ) defaults to 1.0.
#
# size - The shape of the returned array.

x = random.exponential(scale=2, size=(2, 3))
print(x)
sns.distplot(random.exponential(size=10000), hist=False)

plt.show()

# Chi Square distribution is used as a basis to verify the hypothesis.

# It has two parameters:

# df - (degree of freedom).

# size - The shape of the returned array.

x = random.chisquare(df=2, size=(2, 3))
print(x)
sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()

# Rayleigh Distribution
# Rayleigh distribution is used in signal processing.

# It has two parameters:

# scale - (standard deviation) decides how flat the distribution will be default 1.0).

# size - The shape of the returned array.

x = random.rayleigh(scale=2, size=(2, 3))
sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()

# Pareto Distribution
# A distribution following Pareto's law i.e. 80-20 distribution (20% factors cause 80% outcome).

# It has two parameter:

# a - shape parameter.

# size - The shape of the returned array.

sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()

# Zipf distritutions are used to sample data based on zipf's law.

# Zipf's Law: In a collection the nth common term is 1/n times of the most common term.
# E.g. 5th common word in english has occurs nearly 1/5th times as of the most used word.
# It has two parameters:

# a - distribution parameter.

# size - The shape of the returned array.

x = random.zipf(a=2, size=1000)
sns.distplot(x[x < 10], kde=False)
plt.show()




