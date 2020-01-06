log = [int(i) for i in input().split()]
difflog = set(log)
if len(log) == len(difflog):
    print("All are different")
print("Not different")
