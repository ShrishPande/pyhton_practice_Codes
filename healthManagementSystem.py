def getdate():
    import datetime
    return datetime.datetime.now()

def append(clientName):
    c = int(input("Press 1 for exercise and 2 for food"))
    if c==1:
        value= input("Type Here\n")
        with open(f"{clientName}-ex.txt","a") as op:
            op.write(str(str(getdate())+": "+value+ "\n"))
        print("Succesfully Written")
    elif c==2:
        value = input("Type Here\n")
        with open(f"{clientName}-food.txt","a") as op:
            op.write(str(str(getdate())+": "+value+ "\n"))
        print("Succesfully written")

def retrieve(clientName):
    c = int(input("Press 1 for exercise and 2 for food"))
    if c==1:
        with open(f"{clientName}-ex.txt") as op:
            for i in op:
                print(i,end="")
    elif c==2 :
        with open(f"{clientName}-food.txt") as op:
            for i in op:
                print(i, end="")


def clientlist():
    b= int(input("Press 1 for harry 2 for Rohan and 3 for Hammad"))
    return b

print("----Health Management System----")

a= int(input("Press 1 for lock the value , 2 for retrieve te value"))

if a==1:
    k = clientlist()
    if k==1:
        a = "Harry"
        append(a)
    elif k==2:
        a = "Rohan"
        append(a)
    elif k==3:
        a="Hammad"
        append(a)
    else:
        print("Enter a valid input")
        clientlist()
else:
    k = clientlist()
    if k==1:
        a = "Harry"
        retrieve(a)
    elif k==2:
        a = "Rohan"
        retrieve(a)
    elif k==3:
        a="Hammad"
        retrieve(a)
    else:
        print("Enter a valid input")
        clientlist()