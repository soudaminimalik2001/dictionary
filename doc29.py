dict={"a":[1,2,3],"c":[1,0,9],"b":[5,6,2]}
sorted_dict={}
for i,j in dict.items():
    sorted_dict ={i:sorted(j)}
    print(sorted_dict)