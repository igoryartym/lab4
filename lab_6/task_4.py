n = int(input("n = "))
vect1 = [int(input()) for x in range(n)]
print(vect1)
vect2 = [int(input()) for x in range(n)]
print(vect2)
for i in range(n):
    if i != n-1:
        if vect1[i] / vect2[i] != vect1[i+1] / vect2[i+1]:
            print("Вектори не паралельні!")
            break
else:
    print("Вектори паралельні!")
