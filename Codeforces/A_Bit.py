n = int(input())
operations = []

for i in range(n):
    operations.extend(input().split('X'))

x = 0
for op in operations:
    if op == '++':
        x += 1
    elif op == '--':
        x -= 1

print(x)
