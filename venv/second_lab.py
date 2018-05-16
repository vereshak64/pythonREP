from openpyxl import load_workbook
from matplotlib import pyplot
wb = load_workbook('data\data_analysis_lab.xlsx')
sheet = wb['Data']
sheet['A'][1:]
def getvalue(x):
    return x.value
x = list(map(getvalue, sheet['A'][1:]))
y = list(map(getvalue, sheet['B'][1:]))
print(x)
print(y)