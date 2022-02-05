dict={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
for i in dict:
    for j in range(len(dict[i])):
        if j%2!=0:
            dict.pop
    print(dict)
            