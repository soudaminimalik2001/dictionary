list = [1, 2, 3, 4]
#Sample output:{1: {2: {3: {4: {}}}}}
# dict1={}
# dict2={}
# dict3={}
# dict4={}
# for i in list:
#     dict1=i
#     print(dict1)
dict={}
new_dict=dict
for i in list:
    new_dict[i]={}
    new_dict=new_dict[i]
print(dict)
