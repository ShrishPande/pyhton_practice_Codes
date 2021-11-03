d1 = {
    "Shrish" : "I am a programmer",
    "om" :"I am a youtuber"
}

a=int(input("Enter 1 for using dictionary ,Enter 2 for entering something in dictionary"))

if a==1:
    key = input("Enter the key")
    print(d1[key])

elif a==2:
    key =input("Enter the key\n")
    value=input("Enter the value\n")
    d1[key]=value
    print(d1)
