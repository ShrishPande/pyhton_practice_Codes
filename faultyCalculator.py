a = int(input("Enter the first Number\n"))
b = int(input("Enter the second Number\n"))

x=int(input("Enter 1 for addition\nEnter 2 for substraction\nEnter 3 for multiplication\nEnter 4 for division"))


if a==45 and b==3 :
    print("45*3=555")
elif a==56 and b==9:
    print("56+9=77")
elif a==56 and b==6:
    print("56/6=4")
else:
    if x==1:
        c=a+b
        print(f'{a}+{b}={c}')
    elif x==2:
        c=a-b
        print(f'{a}-{b}={c}')
    elif x==3:
        c=a*b
        print(f'{a}*{b}={c}')
    elif x==4:
        c=a/b
        print(f'{a}/{b}={c}')
    else:
        print("Enter a valid operator")