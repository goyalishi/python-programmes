# a triangle is valid if sum of two sides is greater than the third side.
a = int(input("Input the first side of a triangle: "))
b = int(input("Input the second side of a triangle: "))
c = int(input("Input the third side of a triangle: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("Yes, This is a valid triangle.")
else:
    print("No, This is not a valid triangle.")