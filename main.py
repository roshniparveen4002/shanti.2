num1 = float(input ("enter first number:"))
num2 = float(input ("enter second number"))
print("choose operators")
print("1. addition ")
print("2. subtraction")
print("3. multiplication ")
print("4. divison ")
print("chhose from the above options")

choice = int(input ("enter choice (1/2/3/4):"))
if(choice ==1):
    result=num1+num2
    print(result)
elif (choice ==2):
    result=num1-num2
    print(result)
elif (choice ==3):
    result=num1*num2
    print(result)
elif(choice==4):
    result=num1/num2
    print(result)
else:
    print("invalid operation")