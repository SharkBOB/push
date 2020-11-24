import pandas as pd
import numpy as np
import mysql.connector

mydb=mysql.connector.connect(host='192.168.1.118',user='root',password='root1234',database='daniel')

mycursor=mydb.cursor()

sql=''
val=()
mycursor.execute(sql,val)
mycursor.execute('SELECT * FROM customers')
myresult=mycursor.fetchall()
for x in myresult:
    print(x)

mydb.commit()
