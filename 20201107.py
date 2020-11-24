import scipy
from scipy import constants

print(constants.liter)
print(scipy.version)
print(constants.pi)
# print(dir(constants))
# print(constants.kibi)    #1024
# print(constants.mebi)    #1048576
# print(constants.gibi)    #1073741824
# print(constants.tebi)    #1099511627776
# print(constants.pebi)    #1125899906842624
# print(constants.exbi)    #1152921504606846976
# print(constants.zebi)    #1180591620717411303424
# print(constants.yobi)    #1208925819614629174706176

# Find the root of equation x+cos(x)

from math import cos
from scipy.optimize import root


def equation(x):
    return x + cos(x)


myroot = root(equation, 0)
print(myroot.x)

# Minimize the function x^2+x+2 with BFGS

# from scipy.optimize import minimize
#
#
# def eqn(x):
#     return x ** 2 + x + 2
#
#
# mymin = minimize(eqn, 0, method='BFGS')
# print(mymin)

from scipy.sparse import csr_matrix
import numpy as np

arr = np.array([0, 0, 0, 0, 0, 0, 1, 2, 45, 1])
print(csr_matrix(arr))

# How to Work With Sparse Data
# SciPy has a module, scipy.sparse that provides functions to deal with sparse data.
#
# There are primarily two types of sparse matrices that we use:
#
# CSC - Compressed Sparse Column. For efficient arithmetic, fast column slicing.
#
# CSR - Compressed Sparse Row. For fast row slicing, faster matrix vector products

# Sparse Matrix Methods
# Viewing stored data (not the zero items) with the data property:

arr1 = np.array([[0, 0, 1], [0, 0, 14], [23, 5, 1]])
print(csr_matrix(arr1).count_nonzero())
print('---------')

# Removing zero-entries from the matrix with the eliminate_zeros() method:
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.eliminate_zeros()
print(mat)
print('---------')

# Eliminating duplicates by adding them:
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
mat = csr_matrix(arr)
mat.sum_duplicates()
print(mat)
print('--------')

# Converting from csr to csc with the tocsc() method:
arr = np.array([[23, 13, 1], [1, 3, 43], [3434, 13, 4]])
newarr = csr_matrix(arr).tocsc()
print(newarr)

# Use the dijkstra method to find the shortest path in a graph from one element to another.

# It takes following arguments:
# return_predecessors: boolean (True to return whole path of traversal otherwise False).
# indices: index of the element to return all paths from that element only.
# limit: max weight of path.
from scipy.sparse.csgraph import dijkstra

arr = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])
newarr = csr_matrix(arr)
print(dijkstra(newarr, return_predecessors=True, indices=0))

# Floyd Warshall
# Use the fold_warshall() method to find shortest_path between all pairs of elements

from scipy.sparse.csgraph import floyd_warshall

arr = np.array([
    [0, 1, 2],
    [1, 0, 0],
    [2, 0, 0]
])
newarr = csr_matrix(arr)
print(floyd_warshall(newarr, return_predecessors=True))

# Bellman Ford
# The bellman_ford() method can also find the shortest path between all pairs of elements,
# But this method can handle negative weights as well.

# Depth First Order
# The depth_first_order() method returns a depth first traversal from a node.
#
# This function takes following arguments:
#
# the graph.
# the starting element to traverse graph from.
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
    [1, 2, 43, 1],
    [23, 23, 4, 1],
    [32, 23, 4, 1],
    [0, 1, 30, 1]
])

newarr = csr_matrix(arr)
print(depth_first_order(newarr, 1))

# Breadth First Order
# The breadth_first_order() method returns a breadth first traversal from a node.
#
# This function takes following arguments:
#
# the graph.
# the starting element to traverse graph from.

from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
    [1, 2, 4, 5],
    [2, 3, 0, 7],
    [0, 35, 5, 6],
    [1, 23, 0, 0]
])

newarr = csr_matrix(arr)
print(breadth_first_order(newarr, 1))

# KDTrees
# KDTrees are a datastructure optimized for nearest neighbor queries.
#
# E.g. in a set of points using KDTrees we can efficiently ask which points are nearest to a certain given point.
#
# The KDTree() method returns a KDTree object.
#
# The query() method returns the distance to the nearest neighbor and the location of the neighbors.
# Find the nearest neighor to point(1,1):

from scipy.spatial import KDTree

points = [(6, -6), (5, 5), (-8, 3), (2, 5)]
kdtree = KDTree(points)
res = kdtree.query((1, 1))
print(res)
print('--------------')
# The function interp1d() is used to interpolate a distribution with 1 variable.
#
# It takes x and y points and returns a callable function that can be called with new x and returns corresponding y.

from scipy.interpolate import interp1d

xs = np.arange(10)
ys = 2 * xs + 1

print(xs)

print(np.arange(2.1, 3, 0.1))
interp_func = interp1d(xs, ys)
newarr = interp_func(np.arange(2.1, 5, 0.1))
print(newarr)

# Spline Interpolation
# In 1D interpolation the points are fitted for a single curve whereas
# In Spline interpolation the points are fitted against a piecewise function defined with polynomials called splines.
#
# The UnivariateSpline() function takes xs and ys and produce a callable funciton that can be called with new xs.

# Interpolation with Radial Basis Function
# Radial basis function is a function that is defined corresponding to a fixed reference point.
#
# The Rbf() function also takes xs and ys as arguments and produces a callable function that can be called with new xs.

# Interpolate following xs and ys using rbf and find values for 2.1 2.2 2.3 ...2.9

from scipy.interpolate import Rbf
xs=np.arange(10)
ys=xs**2+np.sin(xs)+1

interp_func=Rbf(xs,ys)
newarr=interp_func(np.arange(2.1,3,0.1))

print(newarr)

# T-Test
# T-tests are used to determine if there is significant deference between means of two variables. and lets us know if they belong to the same distribution.
#
# It is a two tailed test.
#
# The function ttest_ind() takes two samples of same size and produces a tuple of t-statistic and p-value.

from scipy.stats import ttest_ind
v1=np.random.normal(size=100)
v2=np.random.normal(size=100)

res=ttest_ind(v1,v2)
print(res)

# KS-Test
# KS test is used to check if given values follow a distribution.
#
# The function takes the value to be tested, and the CDF as two parameters.
#
# A CDF can be either a string or a callable function that returns the probability.
#
# It can be used as a one tailed or two tailed test.
#
# By default it is two tailed. We can pass parameter alternative as a string of one of two-sided, less, or greater.

from scipy.stats import kstest

v=np.random.normal(size=100)
res=kstest(v,'norm')

print(res)



# Statistical Description of Data
# In order to see a summary of values in an array, we can use the describe() function.
#
# It returns the following description:
#
# number of observations (nobs)
# minimum and maximum values = minmax
# mean
# variance
# skewness
# kurtosis

from scipy.stats import describe

v=np.random.normal(size=1000)
res=describe(v)
print(res)

# Normality Tests (Skewness and Kurtosis)
# Normality tests are based on the skewness and kurtosis.
#
# The normaltest() function returns p value for the null hypothesis:
#
# "x comes from a normal distribution".
#
# Skewness:
# A measure of symmetry in data.
#
# For normal distributions it is 0.
#
# If it is negative, it means the data is skewed left.
#
# If it is positive it means the data is skewed right.
#
# Kurtosis:
# A measure of whether the data is heavy or lightly tailed to a normal distribution.
#
# Positive kurtosis means heavy tailed.
#
# Negative kurtosis means lightly tailed.

from scipy.stats import skew,kurtosis
v=np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))

# Example
# Find if the data comes from a normal distribution
from scipy.stats import normaltest
print(normaltest(v))