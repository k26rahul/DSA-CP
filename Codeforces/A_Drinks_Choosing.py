# https://codeforces.com/problemset/problem/1195/A

from math import ceil

n, k = [int(x) for x in input().split(' ')]

paired = 0
kUnpaired = [False for _ in range(k + 1)]

for _ in range(n):
    drink = int(input())
    if kUnpaired[drink]:
        paired += 1
        kUnpaired[drink] = False
    else:
        kUnpaired[drink] = True

print(paired * 2 + ceil(n / 2) - paired)
