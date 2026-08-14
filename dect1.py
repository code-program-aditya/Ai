d={1:'Ram', 2:'ITM', 3:'Gwalior', 4:'MP'}
#len
print(len(d))
#get
print(d.get(2))
print(d.get(1,'Ramesh'))
#keys
print(d.keys())
for  k in d.keys():
    print(d[k])
#values
print(d.values())
for v in d.values():
    print(v)
#items
print(d.items())
for k,v in d.items():
    print(k,'-->',v)