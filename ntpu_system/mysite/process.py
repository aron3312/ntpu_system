import csv
import pandas as pd
import numpy as np
import json

#handle nodes
# x=pd.read_csv('D:/award.csv')
# num= [3]
# [num.append(p) for p in range(7,115)]
# pt= x.iloc[:,num]
# allall=[]
# for g in num:
#     all= [allall.append(a) for a in x.iloc[:,g] if a is not np.nan]
# allall = set(allall)
#
# final = []
# for b in allall:
#     dica = {"name":b,"group":1}
#     final.append(dica)
#     dica={}
#print(final)
#print( [ x for x in iter(allall) ])
#for i in range(0,(len(allall))):
    #print(i)

with open('D:/award.csv', newline='',encoding="UTF-8") as csvfile:
   spamreader = csv.reader(csvfile, delimiter=',')
   pp=[]
   personDF = []
   dicc = {}
   for row in spamreader:
       pp.append(row)
   pp2 = pp[1:(len(pp))]
   for row in pp2:
       #print(row)
       a=row[7:114]
       #t = [b for b in a if b !="NA"]
       for b in a:
           if b=="NA":
               continue
           else:
               dicc['source'] = row[3]
               dicc['target']= b
               personDF.append(dicc)
               dicc ={}


result = [dict(t) for t in set([tuple(d.items()) for d in personDF])]
##print(result)
student_name = ""
result = [p for p in result if p['source']==student_name]
print(result)
allall = []
for p in result:
    for k, v in p.items():
        allall.append(v)
allall = set(allall)
allall =  [ x for x in iter(allall) ]
final = []
for b in range(0,len(allall)):
    dica = {"name":allall[b],"group":1}
    final.append(dica)
    dica={}
print(len(allall))
which = lambda lst:list(np.where(lst)[0])
final2 = []
for l in result:
    source = int(which(list(map(lambda x:x==l['source'],allall)))[0])
    target = int(which(list(map(lambda x:x==l['target'],allall)))[0])
    dipp = {"source":source,"target":target,"weight":1}
    final2.append(dipp)
    dipp={}
tojson_data = {"nodes":final,"links":final2}

with open('D:/data123.json', 'w') as outfile:
    a =json.dumps(tojson_data, ensure_ascii=False)
    outfile.write(a)
