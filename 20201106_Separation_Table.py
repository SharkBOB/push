import pandas as pd

"""
Seqaration the table

"""
# wb = pd.read_excel(r'rowdata分工作簿.xlsx')
# col = wb['Reporting Date'].unique()
# print(col)

# new_wb = pd.ExcelWriter('NewSeparation.xlsx')
# for x in col:
#     child_wb = wb[wb['Reporting Date'] == x]
#     newx=str(x)
#     newx=newx.replace('/','_')
#     child_wb.to_csv(new_wb, index=False, sheet_name=newx)
# new_wb.save()
# print('OK')

# ----------------------------------------
# wbtest = pd.read_excel(r"TestData.xlsx")
# data = wbtest.head(5)
# wbtest.drop(1)
# print(data)

"""USE OPENYXL OPERATION THE EXCEL"""
from openpyxl import load_workbook
import openpyxl
# wb = load_workbook("example.xlsx")
# ws = wb.get_sheet_by_name("demo")
# ws.delete_rows(2) # remove the second row
# ws.delete_rows(2, 2) # remove second row,and the next row ,two rows total.
# ws.insert_cols(3) # insert one columns in the third columns next.
# wb.save("example.xlsx")
