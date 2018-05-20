import openpyxl
import glob
import re
import ipaddress

# Структура данных
data = {}

# область видимости!!!!
dir = glob.glob('C:\\Users\\da.vereshchak\\Seafile\\p4ne_training\\config_files\\*.txt')
for file in dir:
   config = open(file)
   for config_row in config:
       if bool(re.match(r'hostname ', config_row)):
           data[config_row.strip(" hostname\n")] = {}
           host = config_row.strip(" hostname\n")
       if bool(re.match(r'interface ', config_row)):
           if config_row.strip(' interface').strip() not in data[host]:
               data[host][config_row.strip(' interface\n')] = ''
               #data[host]["interface"] = {'name': config_row.strip(' interface\n')}
               intf = config_row.strip(' interface\n')
           else: print("Повтор")
       if bool(re.match(r' ip address (([0-9]{1,3}\.){3}[0-9]{1,3})', config_row)):
           data[host][intf] = ipaddress.IPv4Interface(config_row.strip(' ip address \n').replace(' ', '/'))
           #data[host]['interface']['ip address'] = ipaddress.IPv4Interface(config_row.strip(' ip address \n').replace(' ', '/'))
   config.close()

   # Проверочная
   # конструкция

wb = openpyxl.Workbook()
al = wb.active
al = wb.create_sheet('first sheet', 0)
al.title = 'first sheet title'
width = al.column_dimensions['A']
width.width = 21

L = list()
for i in data:
    print(i + "\n")
    temp = [i]
    al.append([])
    al.append(temp)
    al.append([])
    for j in data[i]:
        temp1 = [j, str(data[i][j])]
        #al.append(j + ": " + data[i][j])
        al.append(temp1)
        print(j + ": " + str(data[i][j]))
        if data[i][j]:
            L.append(data[i][j])
print(len(L))

wb.save("sample.xlsx")