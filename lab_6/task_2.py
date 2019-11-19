import math
b = float(input("Введіть b: "))
i = int(input("Введіть i: "))
arr = []
sum = 0

for j in range(1, i+1):
    sum += math.factorial(j) * math.sin(j * b)
    arr.append(sum)

print(arr)
print("Мінімальний: " + str(min(arr)))