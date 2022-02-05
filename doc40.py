list=['S001', 'S002', 'S003', 'S004']
list1=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list2=[85, 98, 89, 92]
#o/p:-[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

d1={}
for i in range(len(list1)):
    #print(list1[i])
    d1[list1[i]]=list2[i]
#print(d1)
d={}
list3=[]
for k,l in d1.items():
    #print(k,l)
    for j in range(len(list)):
        d[list[j]]=d1
#yprint(d)
list3.append(d)
print(list3)