arr = [float(x) for x in input("Введіть список: ").split()]
min_arr = arr[0]
for i in arr:
    if i > 0 and i < min_arr:
        min_arr = i
print(min_arr)