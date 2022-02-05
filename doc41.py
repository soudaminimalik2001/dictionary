dict={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}
d={}
a=()
for i in dict:
    for j in dict[i]:
        print(j)
        if type(j)==float:
            if j>6:
                a=j
                print(a)
        if type(j)==int:
            if j>70:
                a=j
                print(a)
