u=input("enter number")
dict={}
for i in range(len(u)):
    if u[i]=="0":
        dict["zero"]="0"
    if u[i]=="1":
        dict["one"]="1"
    if u[i]=="2":
        dict["two"]="2"
    if u[i]=="3":
        dict["three"]="3"
    if u[i]=="4":
        dict["four"]="4"
    if u[i]=="5":
        dict["five"]="5"
    if u[i]=="6":
        dict["six"]="6"
    if u[i]=="7":
        dict["seven"]="7"
    if u[i]=="8":
        dict["eight"]="8"
    if u[i]=="9":
        dict["nine"]="9"
print(dict)
#user=123
#o/p:-{"one":1,"two":2,"three":3}

# from numpy import s_


# u=input("enter number")
# dict={}
# i=0
# s=""
# while i < len(u):
#     if u[i]=="0":
#         s="zero"
#     if u[i]=="1":
#         s="one"
#     if u[i]=="2":
#         s="two"
#     if u[i]=="3":
#         s="three"
#     if u[i]=="4":
#         s="four"
#     if u[i]=="5":
#         s="five"
#     if u[i]=="6":
#         s="six"
#     if u[i]=="7":
#         s="seven"
#     if u[i]=="8":
#         s="eight"
#     if u[i]=="9":
#         s="nine"
#     i+=1
#     dict[s]=s
# print(dict)