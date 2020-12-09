import numpy as np
import matplotlib.pyplot as plt

# Fit the value using define function
# Seed the random number generator for reproducibility

np.random.seed(0)
x_data = np.linspace(-5, 5, num=50)
y_data = 2.9 * np.sin(1.5 * x_data) + np.random.normal(size=50)

# Now fit a simple sine function to the data

from scipy import optimize


def func(x, a, b):
    return a * np.sin(b * x)


# Training the fit function

params, params_covariance = optimize.curve_fit(func, x_data, y_data)
print(params, params_covariance)
a = params[0]
b = params[1]
# And plot the resulting curve on the data
# params object will pass two parameters,Corresponding a,b

plt.figure(figsize=(6, 4))
plt.scatter(x_data, y_data, label='Data')

plt.plot(x_data, func(x_data, a, b), 'y', label='Fitted function')
plt.legend(loc='best')
plt.show()

# Additional the method name avoid 'test' character
