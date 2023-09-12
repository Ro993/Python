x=20
y=20
z=2
if x+y>z and x+z>y and y+z>x:
    if x==y==z:
        print("traingle is equilateral")
    elif(x==y or x==z or y==z):
        print("triangle is isosceles")  
else:
     print("provide a valid value")    