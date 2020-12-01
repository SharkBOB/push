
# My First Code
# def satisfaction(num1, num2):
#     num = num1 + num2
#     return num
#
#
# print(satisfaction(2, 3))
#
# for i in range(2, 100):
#     print(i)
#
# lis = [2, 3, 4, 2]
#
# for i in lis:
#     print(i)
#
# count = 0
# while True:
#     print(count)
#     count += 1
#     if count > 5:
#         break
# count = 0
# while count < 10:
#     count += 1
#     print(count)
#
# phonebook={}
# phonebook['john1']='12125454'
# phonebook['john2']='45456566'
# phonebook['john3']='54245645'
#
# print(phonebook)
#
# for name,number in phonebook.items():
#     print('phone number of %s %s'%(name,number))
#
# a=set([2,3,4])
# print(a)
#
# b=set(['23','232','2323'])
# print(b)
#
# for i in b:
#     print(i)

import pandas as pd
import numpy as np

# df1=pd.read_excel('TestData.xlsx',index_col=2)
#
# pd.set_option('max_columns',10)
# pd.set_option('max_rows',20)
#
# print(df1)


# for i in range(0,len(l)) :
#     for j in range(0,len(s)):
#         for k in range(0,len(w)):
#             if l[i]==s[j]==w[k]:
#                 print(l[i])
#                 break

from sympy import *


def test(a, b):
    return a + b


c = test(2, 3)
print(c)

a = set(['2', '2', '3'])
b = set(['3', '1'])
print(a.difference(b))
print(b.symmetric_difference(a))


def QuadraticFunction(a, b, c, x):
    return a * x * x + b * x + c


print(QuadraticFunction(2, 3, 4, 1))

# fx=symbols('x')
# FX=fx.integrate(fx,fx(1,2))
# pd.read_excel()

# s = {"code":"200","data":{"desc":"轩逸 2018款 1.6XV CVT尊享版",
# "family":"轩逸",
# "make":"东风日产",
# "msrp":137800,
# "retail":84750,
# "wholesale":78750},
# "message":"成功"}
# print(s['code'])
# print(s['data']['family'])

import pandas as pd


def func1(path):
    # 创建最终返回的空字典
    df_dict = {}
    # 读取Excel文件
    df = pd.read_excel(path)

    df_list = []
    for i in df.index.values:
        # loc为按列名索引 iloc 为按位置索引，使用的是 [[行号], [列名]]
        df_line = df.loc[i, ['省（直辖市）', '市', '市-EN', 'city', 'province', '省会']].to_dict()
        # 将每一行转换成字典后添加到列表
        df_list.append(df_line)
    df_dict['data'] = df_list
    return df_dict


s = func1('城市省份.xlsx')
print(s['data'])
k = s['data']
i = 0
for i in k:
    print(i['city'])

# df2=pd.read_excel(open('城市省份.xlsx','rb'),sheet_name='Sheet1')
# print(df2)


# def fun2(name):
#     dic={}
#     s=pd.read_excel(name)
#     list2=[]
#     for i in s.index.values:
#         sline=s.loc[i,['','']].to_dict()
#         list2.append(sline)
#     dic['data1']=list2
#     return dic

# for i in range(10):
#     if i<=5:
#         print(i)
#     else:
#         break

# Calculate the integration
from sympy import *
import numpy as np

x = symbols("x")
print(int(integrate(x ** 2, (x, 1, 2))))

s = np.array([2, 3])
print(a)

w = [1, 2, 3, 4, 4, 3, 2, 1]
s = []

for i in range(int(len(w) / 2)):
    for j in range(int(len(w) / 2)):
        if w[i] == w[int(len(w)) - (j + 1)]:
            s.append(w[i])
print(s)

dic = {}
dic['data'] = 1
dic['name'] = 'jack'
print(dic)
print(dic['data'])


#
# class a ():
#     def __init__(self,name,age):
#         self.name=name+"slef"
#         self.age=age+10
#
# p=a("jack",10)


def show(s1):
    count = 0
    for i in range(int(len(s1))):
        count = s1[i] + count
    return (count)


list1 = [2, 3, 4, 5, 2]

print(show(list1))

dic1 = {'data': 1232, 'data1': 123124}
print(dic['data'])
for i in dic1.keys():
    print(i)
for i in dic1.items():
    print(i)
for i in dic1.values():
    print(i)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('max_columns', 50)

s = pd.Series([6, 'Heisenberg', 3.14, -1789710578, 'Happy day'])
print(s)


#
# for (k,v) in dic1.items():
#     print("dict[%s]=" % k,v)

# init method or constructor
class Person:
    def __init__(self, name):
        self.name = name + 'BBQ'

    def sayhi(self):
        print('Hello my name is ', self.name)


p = Person('john')
p.sayhi()
