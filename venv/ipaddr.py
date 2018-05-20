from ipaddress import IPv4Network
import random
import pprint

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        octmaxima = random.randint(0x0B000000, 0xDF000000)
        oct1 = random.randint(11, 223)
        oct2 = random.randint(0, 255)
        oct3 = random.randint(0, 255)
        oct4 = random.randint(0, 255)
        addr = str(oct1) + "." + str(oct2) + "." + str(oct3) + "." + str(oct4)
        mask = random.randint(8, 24)
        IPv4Network.__init__(self, address=(addr, mask), strict=False)
    def regular(self):
        return self.is_global
    def key_value(self):
        return int(self.network_address) + (int(self.netmask) << 32)
        #return str(self.prefixlen) + str(self.network_address)

def sortfunc(x):
    return x.key_value()

i=1
L = []
print(len(L))
while len(L) < 20:
    obj = IPv4RandomNetwork()
    if obj.regular():
        L.append(obj)
        print("№%2d" % i, obj, obj.regular())
        print(obj.key_value())
        i += 1
print(len(L))
print("\n")

for i in sorted(L, key=sortfunc):
    print(i)


