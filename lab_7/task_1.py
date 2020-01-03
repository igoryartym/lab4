n = int(input("К-сть рядків: "))
m = int(input("К-сть стовпчів: "))
A = [[int(input("A[{0}][{1}] = ".format(i,j))) for j in range(1, m + 1)] for i in range(1, n + 1)]
for k in A:
    print(k)
s = 0
for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 1 and A[i][j] > 0:
            s += A[i][j]
print("Сума додатніх не парних елементів = {0}".format(s))