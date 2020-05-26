import copy
import re
import datetime
import copy
import configuration as conf
import re

import matplotlib.dates as md
import matplotlib.pyplot as plt
from datetime import datetime
import math
import time
import copy


def picrep(fname):
    f1=open(fname,"r")
    lines=f1.readlines()
    f2=open("tm.txt","w+")
    c=False
    for i in lines:
        if "-- ME:" in i:
            c=True
        elif "/# exit" in i or re.match(r"@$",i):
            c=False
        elif c==True:
            f2.write(i)
    f2.close()
    f2=open("tm.txt","r")
    line=f2.readlines()
    n=0
    for i in line:
        i=i.strip()
        if re.match(r"^QCA IEEE .*",i):
            ip=i[24:41]
        elif  re.match(r"^-- DB (.*):",i):
            n=int(i[7:9])
    
    f2=open("tm.txt","r")
    line=f2.readlines()
    sat=[]
    rel=[]
    ups=[]
    j=1
    for i in line:
        i=i.strip()
        if re.match(r"^#"+str(j)+": QCA IEEE .*",i):
                sat.append(i[28:45])
                j=j+1
        elif re.match(r"^Relation: .*",i):
                rel.append(i[10:25])
        elif re.match(r"^Upstream Device:.*",i)and "Upstream Device: None" not in i:
                ups.append(i[17:34])

    for i in range(n):
        if rel[i]=="Direct Neighbor" and sat[i] not in ups:
            print(ip+"(Router) <----- "+sat[i]+"(Satellite "+str(i+1)+")")
        else:
            for j in range(n):
                if ups[i]==sat[j]:
                    print(ip+"(Router)<----- "+ups[i]+"(Satellite "+str(j+1)+") <----- "+sat[i]+"(Satellite "+str(i+1)+")")
                    break
        
