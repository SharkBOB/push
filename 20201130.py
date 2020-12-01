import pandas as pd
import mysql.connector

# connect to mysql
mydb=mysql.connector.connect(
    host='192.168.1.118',
    user='root',
    password='root1234',
    database='daniel'
)

MyCursor = mydb.cursor()

# execute the insert process
# --------------------------
sql='insert into customers(name,adress) values (%s,%s)'

val=('john','high way 123456')
MyCursor.execute(sql,val)
print('insert successfully')
# UTF-8 code process
wb = pd.read_csv('HKUniqueVehicle.csv', error_bad_lines=False)
# Get the unique vehicle description
VehicleUniqueDescription = wb['Description']

# Get all data
wb2 = pd.read_csv('HKVehicle.csv', encoding='unicode_escape')
VehicleDescription = wb2['Description']
GoodRetail = wb2['GoodRetail']
YearGroup = wb2['YearGroup']

# print(VehicleDescription)
# Create the list add vehicle prices







