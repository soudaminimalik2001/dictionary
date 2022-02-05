dict={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
#o/p-:{'S001': ['Math', 'Science'], 'S002': ['Math', 'English']} 
# for i in dict.keys():
#     if i==" ":
#         dict.pop
    
d1={}    
for i,j in dict.items():
    for x in " ":
        i=i.replace(x,"")
        d1[i]=j
print(d1)