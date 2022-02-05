dict = {'a':50,'b':58,'c': 56,'d':40,'e':100,'f':20}
#o/p=['e','b','c']
list1=[]
for i in dict.values():
    list1.append(i)
print(list1)
max=0
secondmax=0
thirdmax=0
for i in range(2,len(list1)): 
   if list1[i]>max: 
      secondmax=max
      max=list1[i] 
   elif list1[i]>secondmax: 
         secondmax=list1[i] 
    # elif dict[x]>max2:
    #         max3=dict[x]
    #         max3=max2
    #         a.append(max2)
   elif list1[i]>thirdmax:
         thirdmax=list1[i]
            # a.append(max3)
print(secondmax) 
print(max) 
print(thirdmax)  
        
     
