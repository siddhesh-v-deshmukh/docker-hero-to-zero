print('''
for addition enter 1
for substraction enter 2
for division enter 3
for multiplication enter 4
      ''')
num=int(input("enter the number:-"))
if(num==1):
    a=int(input("enter value of a:-"))
    b=int(input("enter value of b:-"))
    print(a+b)
elif(num==2):
    a=int(input("enter value of a:-"))
    b=int(input("enter value of b:-"))
    print(a-b)
elif(num==3):
    a=int(input("enter value of a:-"))
    b=int(input("enter value of b:-"))
    print(a/b)
elif(num==4):
    a=int(input("enter value of a:-"))
    b=int(input("enter value of b:-"))
    print(a*b)
else:
    print("number entered is invalid!!")
