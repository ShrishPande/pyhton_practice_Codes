try:
    n = int(input("Enter number of rows you want to print"))
    x = int(input("Press 1 for 1st pattern and press 0 for second pattern"))

    a= True

    if x==1:
        a = True
    elif x==0:
        a = False

    if a:
        i=1
        while (i<=n):
            j=1
            while (j<=i):
                print("*",end=" ")
                j+=1
            print()
            i+=1 
    else:
        i=n
        while(i>=1):
            j=1
            while(j<=i):
                print("*",end=" ")
                j+=1
            print()
            i-=1

except Exception as e:
    print(e)