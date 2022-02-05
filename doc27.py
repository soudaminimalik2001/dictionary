student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
#o/p:-6
# c=0
# for i in student:
#     if i['id'] in student:
#         c+=i['id']
# prin(c)
print(sum(d['id']for d in student))

# c=0
# for i in student:
#     for j in student:
#         if 
             