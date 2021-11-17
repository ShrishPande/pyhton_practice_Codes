num=int(input("Enter Your Number"))
for i in range(1,num+1):
    for j in range(i,num):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    for l in range(i-1):
        print("*",end="")
    print()
for j in range(1,num):
    for x in range(j):
        print(" ",end="")
    for y in range(j,num):
        print("*",end="")
    for z in range(j+1,num):
        print("*",end="")
    print()