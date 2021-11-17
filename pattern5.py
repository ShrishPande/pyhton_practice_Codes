num = int(input("Enter Your Number"))
for i in range(1,num+1):
    for j in range(i,num):
        print(" ",end="")
    for k in range(1,2*i):
        if k==1 or k==2*i-1 or i==(num//2)+1:
            print("*",end="")
        else:
            print(" ",end="")
    print()