dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# input 3 numbers from user
num1, num2, num3 = map(int, input("Enter 3 Numbers eg(13 4 14): ").split())

# for num 1 is the greatest
if(num1>=num2 and num1>= num3):
    if(num2>=num3):
        print(f"Descending: {num1} {num2} {num3}")
    else:
        print(f"Descending: {num1} {num3} {num2}")

# for num 2 is the greatest
elif(num2>=num1 and num2>= num3):
    if(num1>=num3):
        print(f"Descending: {num2} {num1} {num3}")
    else:
        print(f"Descending: {num2} {num3} {num1}")

# for num 3 is the greatest
else:
    if(num2>=num1):
        print(f"Descending: {num3} {num2} {num1}")
    else:
        print(f"Descending: {num3} {num1} {num2}")
