x, y = 0, 0

M = []

for i in range(5):
    k = input().split()
    if '1' in k:
        x = i + 1
        y = k.index('1') + 1
        break

print(abs(x - 3) + abs(y - 3))
