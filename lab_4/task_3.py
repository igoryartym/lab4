import math
x1 = float(input("input x1:"))
y1 = float(input("input y1:"))
x2 = float(input("input x2:"))
y2 = float(input("input y2:"))
x3 = float(input("input x3:"))
y3 = float(input("input y3:"))
a = math.sqrt(x1*x1+y1*y1)
b = math.sqrt(x2*x2+y2*y2)
c = math.sqrt(x3*x3+y3*y3)
if a == b == c:
    print("True")
else:
    print("False")

