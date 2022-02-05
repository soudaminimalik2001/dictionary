a="MISSISSIPPI"
j=list(a)
print(j)
c={}
for i in j:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)
#o/p={'M':1,'I':4,'S':4,'p':2}
        
    