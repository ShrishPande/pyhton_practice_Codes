num =int(input("Enter yor number"))
for i in range(1,num+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(2*i,2*num+1):
        print("*",end="")
    print()