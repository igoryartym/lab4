a = float(input("input a:"))
b = float(input("input b:"))
c = float(input("input c:"))

if a > b:
    max_ab = a
else:
    max_ab = b

if b < c:
    min_bc = b
else:
    min_bc = c

print(max_ab * min_bc**2)
