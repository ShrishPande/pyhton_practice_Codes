x1=int(input("Enter X coordinate of Bigger Circle\n"))
y1=int(input("Enter y coordinate of Bigger Circle\n"))
x2=int(input("Enter X coordinate of Smaller Circle\n"))
y2=int(input("Enter y coordinate of Smaller Circle\n"))

R=int(input("Enter radius of Bigger circle\n"))
r=int(input("Enter radius of Smaller circle\n"))

d=((x1-x2)**2+(y1-y2)**2)**0.5

if d+r<R:
    print("Smaller Circle is completely inside the bigger Circle without touching the circumference")

elif d+r==R:
    print("Smaller Circle is completely inside the bigger Circle and touching the circumference")

elif d+r>R:
    print("Smaller Circle is outside the bigger Circle")

else :
    print("Smaller circle is outside the bigger circle")