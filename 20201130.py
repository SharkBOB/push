import pandas as pd
import mysql.connector

# connect to mysql
mydb = mysql.connector.connect(
    host="192.168.1.118",
    user="root",
    password="root1234",
    database="daniel"
)

MyCursor = mydb.cursor()

# --------------------------
# Get the vehicle information from new data table
# Find the issue prices

def DetemingPrices(res):
    result = list(res)
    # Get the description len
    for i in range(len(result) - 1):
        old_vehicle = res[i]
        new_vehicle = res[i + 1]
        old_vehicle_prices = old_vehicle[2]
        new_vehicle_prices = new_vehicle[2]
        # If the old prices higher than new prices ,return the vehicle key.
        try:
            if int(old_vehicle_prices) > int(new_vehicle_prices):
                return old_vehicle[0]
        except:
            pass


def GetData():
    sql = "SELECT VehicleKey,MakeCode,FamilyCode,Description,COUNT(*) FROM rbvehicle202011 " \
          "GROUP BY MakeCode, FamilyCode,Description"
    MyCursor.execute(sql)
    result = MyCursor.fetchall()
    # print(result)
    # Loop the result for search the vehicle description more than one.
    for i in result:
        vehicle_key, make, family, des, count = i
        if count > 1:
            second_sql = "SELECT Vehiclekey,YearGroup,GoodRetail FROM rbvehicle202011 WHERE MakeCode = '{0}' AND FamilyCode = '{1}'  AND Description = '{2}' ORDER BY YearGroup;".format(
                make, family, des)
            MyCursor.execute(second_sql)
            second_result = MyCursor.fetchall()
            # Determing Prices Issues
            issue_prices_code = DetemingPrices(second_result)
            if issue_prices_code:
                print(issue_prices_code, second_result)
    print("OK")


if __name__ == '__main__':
    GetData()
