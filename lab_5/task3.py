import math
epsilon = float(input("Введіть з якою точністю: "))
while epsilon >= 1:
    print("Введіть правильну точність <1")
    epsilon = float(input("Введіть з якою точністю: "))
x = float(input("Введіть чисельник: "))
s = 1
b = 1
c = 1
a = 1
while math.fabs(a/(b*c)) > epsilon:
    s += (a/(b*c))
    a = a*(-x**2)
    b = b*c*(c+1)
    c += 2
else:
    print("Suma = {0} ".format(round(s,3)))