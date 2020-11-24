import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Fitting a polynomial curve to given value
df = pd.read_excel('NewMargin.xlsx', sheet_name='prices margin using')
ComparePrices = df['ComparePrices']
PricesRatio = df['PricesRatio']

# Scatter plotting
plt.scatter(ComparePrices, PricesRatio, label='Data')

# Get the Polynomial coefficients
fit = np.polyfit(ComparePrices, PricesRatio, 18)
# Get the polynomial
p1 = np.poly1d(fit)
print(fit)
print(p1)

# Calculate the fit PricesRatio value
Y_value = p1(ComparePrices)

# Plotting the curve

plt.plot(ComparePrices, PricesRatio, '*', label='origin value')
plt.plot(ComparePrices, Y_value, 'r', label='poly fit value')
plt.legend(loc='best')
plt.title('poly fit')
plt.show()

# Output the final values
for i in range(len(ComparePrices)):
    print(ComparePrices[i], Y_value[i])
