a=[{"first":"1"},{"second": "2"},{"third": "1"}, {"four": "5"}, {"five":"5"},{"six":"9"},{"seven":"7"}]

list = []
for i in a:
    for j in i.values():
        list.append(j)
print(list)
temp_list=[]
for k in list:
    if k not in temp_list:
        temp_list.append(k)
    else:
        pass
print(temp_list)
        
        
    
