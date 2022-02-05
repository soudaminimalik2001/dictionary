from posixpath import split


dict=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
#Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
dict1=[]
# for i in dict:
#     for j in dict:
#         if j not in dict1:
#             dict1.update(j)
# print(dict1)



for i in dict: 
  for j in i.values():
    dict1.append(j)
print(set(dict1))