num=int(input("Enter te number of lines"))
for i in range(1,num+1):
    for j in range(i-1):
        print(" ",end="")
    for k in range(i,num+1):
        print(k,end="")
    print()