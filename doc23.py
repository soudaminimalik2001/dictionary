dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
# a=[]
max1=0
max2=0
max3=0
for x in dict:
        if dict[x]>max1 :
             max2=max1
             max3=max2
             max1=dict[x]
            #  a.update(max1)
        elif dict[x]>max2:
            max3=max2
            max=dict[x]
            # a.update(max2)
        elif dict[x]>max3:
            max1=dict[x]
            # a.update(max3)
print(max1)
print(max2)
print(max3)
# print(a)