AX=0
AY=0
BX=10
BY=30
CX=20
CY=0

#Taking input from the user
PX=int(input("Enter X coordinate"))
PY=int(input("Enter Y coordinate"))

#Area of the triangle ABC
area =abs((AX*(BY-CY)+BX*(CY-AY)+CX*(AY-BY))*0.5)

#Area of triangle APC

area1 =abs((AX*(PY-CY)+PX*(CY-AY)+CX*(AY-PY))*0.5)

#Area of triangle APB

area2 =abs((BX*(PY-CY)+PX*(CY-BY)+CX*(BY-PY))*0.5)
#Area of triangle BPC

area3 =abs((AX*(PY-BY)+PX*(BY-AY)+BX*(AY-PY))*0.5)
total_area=area1+area2+area3

if area==total_area:
    print("Point P is inside the Triangle")
else:
    print("Point P is outside the Triangle")
