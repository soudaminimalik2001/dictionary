dict={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

# Sample Output:

# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11
for i in dict:
    print(i,end=" ")
print("")
for j in range(len(dict)):
    for k in dict:
        print(dict[k][j],end=" ")
    print()
    
        

# dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# print(*list(dict.keys( )))
# a=(list(dict.values( )))
# for i in range(len(a)):
#     print(*(a[i]))
