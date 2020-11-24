import numpy as np
import sklearn as sk
import matplotlib.pyplot as plt
import pandas

from numpy import array
from sklearn import linear_model

# Data Structure
city = [[{'data1': 123}, {'data2': 124}], {'data1': 125}, {'data2': 126}]

print(city[0][1]['data2'])

city1 = {'data': [123, 1234, {'data5': 128}]}
print(city1['data'][2]['data5'])

reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
reg.coef_
array([0.5, 0.5])
print(array([0.5, 0.5]))

str1 = 'Ilovechina'
print(str1.split())

# Mysql Operation

import pymysql

conn = pymysql.connect("192.168.1.118", user="root", password="root1234", db="daniel")
cursor = conn.cursor()
print(cursor)
s = cursor.execute(
    'CREATE TABLE EMPLOYEE (FIRST_NAME  CHAR(20) NOT NULL,LAST_NAME  CHAR(20),AGE INT,SEX CHAR(1),INCOME FLOAT )')
# w = cursor.execute('select * from Test')
# list = []
# for row in cursor:
# print(list)
# show all lines

# print(list[1][1])

print('Create The Table Successfully')
cursor.close()
conn.close()

# m1=np.array([[2,32,5,5,1,1],[3,3,5,1,4,5]])
# print(m1)
#
# x10=np.random.randint(0,10,(5,5))
# x11=np.random.randint(0,10,(5,5))
# print(x10[1])


for i in range(10):
    print(i)
