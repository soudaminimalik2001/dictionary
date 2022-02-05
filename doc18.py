dict={"a":78,"b":80,"c":50,"d":15}
max=0
min=0
for i in dict:
    if dict[i]>max :
        max =dict[i]
    elif dict[i]>min:
        min=dict[i]
print(max)
print(min)
        