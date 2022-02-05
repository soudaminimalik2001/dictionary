dict={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Length of dictionary values:
# {'red': 3, 'green': 5, 'black': 5, 'white': 5}
def test(dict):
    dict1={}
    for i in dict.values:
        dict1[i]=len(i)
    return dict1
print(dict)
print(test(dict))
