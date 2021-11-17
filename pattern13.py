num =int(input("Enter Your Number"))
for i in range(1,num+1):
    for j in range(65,65+i):
        print(chr(j),end="")
    print()
