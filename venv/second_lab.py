from openpyxl import load_workbook
from matplotlib import pyplot
wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
sheet['A'][1:]
def getvalue():
    return x.value
x = map(getvalue, sheet['A'][1:])
y = map(getvalue, sheet['B'][1:])
print(x)
print(y)
input()