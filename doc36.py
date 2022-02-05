from re import I


d={'key1': 1, 'key2': 3, 'key3': 2} 
d1={'key1': 1, 'key2': 2}
#Expected output: key1: 1 is present in both x and y
for i in d:
    if i in d1:
        if d[i]==d1[i]:
            print(i,':',d[i],"is present in both d and d1")
        
        
