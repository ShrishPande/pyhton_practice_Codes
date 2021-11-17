num = int(input("Enter Your Number"))
for i in range(1,num+1):
    for j in range(i,num):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()