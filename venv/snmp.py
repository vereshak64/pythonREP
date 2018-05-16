from pysnmp.hlapi import *
import pprint

result = getCmd(SnmpEngine(),
                CommunityData(communityIndex=1, communityName='public', mpModel=0),
                UdpTransportTarget(("10.31.70.107", 161)),
                ContextData(),
                ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
                )

result2 = nextCmd(SnmpEngine(),
                CommunityData(communityIndex=1, communityName="public", mpModel=0),
                UdpTransportTarget(("10.31.70.107", 161)),
                ContextData(),
                ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')), lexicographicMode=False
                )
for x in result:
    print(x[3][0])

for y in result2:
    pprint.pprint(y[3])
    for z in y[3]:
        print(z)



