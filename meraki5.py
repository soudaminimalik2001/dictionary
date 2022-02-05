list1=['one','two','three','four','five']
list2=[1,2,3,4,5,]
#0/p-{“one”:1,”two”:2,”three”:3,”four”:4,”five”:5}
c={}
for i in range(len(list1)):
    c[list1[i]]=list2[i]
print(c)