arr = [int(x) for x in input("Введіть список:").split()]
arr1 = list(filter(lambda i: i != 0, arr))
arr1.sort()
num = len(arr) - len(list(arr1))
ans = ([0] * num) + arr1
print(ans)