n = int(input())
count = 0
for x in range(1, n + 1):
    s = (2 * x) ** 2 + (2 * x + 1) ** 3
    count += s
print(count)

