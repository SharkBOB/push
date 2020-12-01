# -*- coding: utf-8 -*- 
# @Author : Lucky 
# @File : 香港车型延续.py
import pymysql

dbb = pymysql.connect('192.168.1.118', 'root', 'root1234', 'daniel', port=3306, charset='utf8')
cursor = dbb.cursor()


def judge_data(res2):
    res2 = list(res2)
    for i in range(len(res2) - 1):
        # code,year,GoodRetail
        # print(res2[i])
        before = res2[i]
        after = res2[i + 1]
        # GoodRetail价格比较
        # Process the exception of GoodRetail is null.
        try:
            if int(before[2]) > int(after[2]):
                return before[0]
        except:
            pass

def get_alldata():
    sql0 = "SELECT VehicleKey,MakeCode,FamilyCode,Description,count(*) as c FROM rbvehicle202011 GROUP BY MakeCode,FamilyCode,Description;"
    cursor.execute(sql0)
    res = cursor.fetchall()

    for s in res:
        VehicleKey, make, family, desc, c = s
        if c > 1:
            sql1 = "SELECT Vehiclekey,YearGroup,GoodRetail FROM rbvehicle202011 WHERE MakeCode = '{0}' AND FamilyCode = '{1}'  AND Description = '{2}' ORDER BY YearGroup;".format(
                make, family, desc)
            cursor.execute(sql1)
            res2 = cursor.fetchall()
            # print(res2)
            # 判断价格是否有问题，如果有，返回第一个出现价格问题的code（年）
            isok = judge_data(res2)
            if isok:
                print(isok,res2)


if __name__ == '__main__':
    get_alldata()
