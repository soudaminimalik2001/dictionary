a='w3resource'
#Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
j=list(a)
print(j)
c={}
for i in j:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)

