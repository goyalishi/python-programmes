import math
x1=int(input("enter x1"))
x2=int(input("enter x2"))
y1=int(input("enter y1"))
y2=int(input("enter y2"))
d=(((x2 - x1 )**2) + ((y2-y1)**2) )
dist=math.sqrt(d)
print("Distance between pointd(%d,%d) and(%d,%d)=%0.2f"%(x1,x2,y1,y2,dist))