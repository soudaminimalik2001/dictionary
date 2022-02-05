students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':3}}
# Sample Output:

# Aex                                                                                                           
# class : V                                                                                                     
# rolld_id : 2                                                                                                  
# Puja                                                                                                          
# class : V                                                                                                     
# roll_id : 3 







# for key in students:

#      print(key)
# for i in students.values():
#     print(i)
    
for i in students:
    print(i)
    for j in students[i]:
        print(j,':',students[i][j])    