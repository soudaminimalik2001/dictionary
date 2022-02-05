#Sample input ( n = 5) :
#Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
user=int(input("enter number"))
dict={}
for i in range(1,user):
    a=i*i
    dict[i]=a
print(dict)
    