dict=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# String values of a given dictionary, into integer types:
# [{'x': 10, 'y': 20, 'z': 30}, {'p': 40, 'q': 50, 'r': 60}]
for i in range(len(dict)):
    for j in dict[i].values():
        if type(j)=="string":
            j=int
print(dict)

