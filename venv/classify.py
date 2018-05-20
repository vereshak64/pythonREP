import glob
import re
import ipaddress

# Структура данных
data = {'ip': [], 'int': [], 'host': []}

# функция классификатор
def classify(row):
    if bool(re.match(r' ip address (([0-9]{1,3}\.){3}[0-9]{1,3})', row)):
        #print(row.strip(' ip address ').strip('\n').replace(' ', '/'))
        return data['ip'].append(ipaddress.IPv4Interface(row.strip(' ip address \n').replace(' ', '/')))
    if bool(re.match(r'interface', row)):
        #print(row.strip('interface'))
        if row.strip(' interface').strip() not in data['int']:
            return data['int'].append(row.strip(' interface\n'))
        #else:
        #    print("Повтор " + str(data['int'].index(row.strip('interface').strip())))
    if bool(re.match(r'hostname ', row)):
        return data['host'].append(row.strip(" hostname\n"))


# Обрати внимание как прописан виндовый путь. Если путь внутри проекта то как не надо, или не обязательно... я чет хз
dir = glob.glob('C:\\Users\\da.vereshchak\\Seafile\\p4ne_training\\config_files\\*.txt')
for file in dir:
   config = open(file)
   for config_row in config:
       classify(config_row)
   config.close()


# Проверочная
# конструкция

print("Длинна ip массива " + str(len(data['ip'])))
data['ip'] = list(set(data['ip'])) # Убираем дубликаты
print("Длинна ip массива " + str(len(data['ip'])))
print(data['ip'])
#print("Длинна int массива " + str(len(data['int'])))
#data['ip'] = list(set(data['ip'])) # Убираем дубликаты
#print("Длинна int массива " + str(len(data['int'])))
print(data['int'])
print(data['host'])