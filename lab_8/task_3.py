n = int(input("Введіть число: "))
x0 = 0#Рекурсія
x1 = 9
if n == 0:
    print("x= 0")
elif n == 1:
    print("x= 9")
else:
    for i in range(n - 1):
        xn = 2 * x1 + 3 * x0
        x0 = x1
        x1 = xn
    print("x(n)= {0}".format(xn))