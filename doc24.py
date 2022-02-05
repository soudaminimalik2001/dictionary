dict=[{'item': 'item1', 'amount': 400}, 
    {'item': 'item2', 'amount': 300}, 
    {'item': 'item1', 'amount': 750}]
#o/p-({'item1': 1150, 'item2': 300})
dict1={}
for i in dict:
    if i['item'] in dict1.keys():
        dict1[i['item']]+=i["amount"]
    else:
        dict1[i['item']]=i["amount"]
print(dict1)
    
        
        

