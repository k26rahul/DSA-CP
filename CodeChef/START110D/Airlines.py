import math

T = int(input())

for _ in range(T):
    x, n = map(int, input().split())

    capacity = x * 100

    if capacity < n:
        print(math.ceil((n - capacity) / 100))
    else:
        print(0)
