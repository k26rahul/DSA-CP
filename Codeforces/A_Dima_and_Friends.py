n = int(input())
fingers = sum(map(int, input().split()))

ways = 0

for i in range(1, 6):
    if (fingers + i) % (n + 1) != 1:
        ways += 1

print(ways)
