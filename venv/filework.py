import glob
import re

# Обрати внимание как прописан виндовый путь. Если путь внутри проекта то как не надо, или не обязательно... я чет хз
dir = glob.glob('C:\\Users\\da.vereshchak\\Seafile\\p4ne_training\\config_files\\*.txt')

print(dir)
ip = []
for file in dir:
   config = open(file)
   for row in config:
       #if row.find('ip address') == 1:
           if bool(re.match(r' ip address.(([0-9]{1,3}\.){3}[0-9]{1,3})', row)):
               ip.append(row.strip(' ip address '))
               print(row.strip(' ip address '))
   config.close()
print(len(ip))
ip = list(set(ip))
print(len(ip))
# x = [] - список
# x = list(set(x))