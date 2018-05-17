from openpyxl import load_workbook
from matplotlib import pyplot
wb = load_workbook('data\data_analysis_lab.xlsx')
sheet = wb['Data']

def getvalue(x):
    return x.value

x = list(map(getvalue, sheet['A'][1:]))
y1 = list(map(getvalue, sheet['C'][1:]))
y2 = list(map(getvalue, sheet['D'][1:]))
print(x)
print(y1)
print(y2)

pyplot.plot(x, y1, 'r--')
pyplot.plot(x, y2, 'b-')
pyplot.show()

'''
m = sheet['A'][1:]
s = list(m)
for i in s:
   print(i)
'''