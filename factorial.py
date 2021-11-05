a =int(input("ENter the number\n"))
f=1
if a<0:
    print("doesnt exist")
elif a==1:
    print("factorial is 1")
else:
    for i in range(1,a+1):
        f=f*i
    print(f"factorial of {a} is {f}")