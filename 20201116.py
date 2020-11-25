import pandas as pd

# Get the dataset from new monthly upgrade

wb = pd.read_excel('RB20201124.xlsx')

# wb.to_excel('newRB.xlsx')
# print(wb.columns)
# print(wb.dtypes)

code = wb['VehicleKey']
year = wb['YearGroup']
GoodRetail = wb['GoodRetail']

# The Margin coefficient

wb2 = pd.read_excel('NewMargin.xlsx', sheet_name='prices margin using')
wb3 = pd.read_excel('NewMargin.xlsx', sheet_name='year margin using')
prices = wb2['ComparePrices']
PricesRatio = wb2['PricesRatio']
YearRatio = wb3['YearRatio']

# Loop the good retail ,get the closest coefficient to the compare prices.

ComparePrices = []
for i in GoodRetail:
    j = min(prices, key=lambda x: abs(x - i))
    ComparePrices.append(j)

# Create the new excel
# Using the merge methodology replace the VLookUp

newdf = pd.DataFrame({'code': code,
                      'year': year,
                      'GoodRetail': GoodRetail,
                      'ComparePrices': ComparePrices})

JoinPricesRatio = newdf.merge(wb2, on='ComparePrices', how='left')
JoinYearRatio = JoinPricesRatio.merge(wb3, on='year', how='left')

# Merge the Prices Ratio and Year Ratio

GoodWhosales = JoinYearRatio['GoodRetail'] / (1 + (JoinYearRatio['PricesRatio'] * JoinYearRatio['YearRatio']))

print(GoodWhosales)

# Create the final excel to useing

finaldf = pd.DataFrame({'code': JoinYearRatio['code'],
                        'year': JoinYearRatio['year'],
                        'GoodRetail': JoinYearRatio['GoodRetail'],
                        'GoodWhosales': GoodWhosales,
                        'ComparePrices': JoinYearRatio['ComparePrices'],
                        'PricesRatio': JoinYearRatio['PricesRatio'],
                        'YearRatio': JoinYearRatio['YearRatio']})
finaldf.to_excel('final20201124.xlsx')
print('OK')
