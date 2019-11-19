n = int(input("Введіть число: "))
x0 = 0
x1 = x2 = 9
if n == 0:
    print("x= 0")
elif n == 1 or n == 2:
    print("x= 9")
else:
    for i in range(n-2):
        xn = x2+4*x0
        x0 = x1
        x1 = x2
        x2 = xn
    print("x(n)= {0}".format(xn))