import mysql.connector
import pandas as pd
import numpy as np

df=pd.read_excel('RB20201204.xlsx')
GoodRetail=df['GoodRetail']
GoodRetail=round(GoodRetail,-2)
print(GoodRetail)


