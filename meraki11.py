dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
#o/p=[58,56,100]
a=[]
max1=0
max2=0
max3=0
for x in dict:
        if dict[x]>max1 :
             max2=max1
             max1 =dict[x]
             max3=max2
             a.append(max1)
        elif dict[x]>max2:
            max2=dict[x]
            # max3=max2
            a.append(max2)
        elif dict[x]>max3:
            max1=dict[x]
            a.append(max3)
# print(max1) 
# a.append(max1)
# print(max2) 
# a.append(max2)
# print(max3)
# a.append(max3) 
print(a)  



# list1 = [10, 20, 4, 45, 99] 

# max=max(list1[0],list1[1]) 
# secondmax=min(list1[0],list1[1]) 

# for i in range(2,len(list1)): 
#    if list1[i]>max: 
#       secondmax=max
#       max=list1[i] 
#    else: 
#       if list1[i]>secondmax: 
#          secondmax=list1[i] 

# print("Second highest number is : ",str(secondmax)) 
    