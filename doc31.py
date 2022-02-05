from curses import KEY_A1


d={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
max1=0
max2=0
max3=0
K1=0
k2=0
k3=0
for i in d:
    if d[i]>max1:
        max1=d[i]
        k1=i
for j in d:
    if d[j]>max2 and d[j]<max1:
        max2=d[j]
        k2=j
for k in d:
    if d[k]>max3 and d[k]<max2:
        max3=d[k]
        k3=k
print(k1,max1)
print(k2,max2)
print(k3,max3)
            
# if dict[x]>max1 :
#              max2=max1
#              max1 =dict[x]
#              max3=max2
#              a.append(max1)
#         elif dict[x]>max2:
#             max2=dict[x]
#             # max3=max2
#             a.append(max2)
#         elif dict[x]>max3:
#             max1=dict[x]        

