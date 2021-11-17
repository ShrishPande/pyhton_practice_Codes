num = int(input("Enter YOur number"))
for i in range(1,num+1):
    for j in range(i,num):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()