import math

T = int(input())

for _ in range(T):
    C, F = map(int, input().split())

    best1 = float('inf')
    for i in range(F):
        newC = C + i
        newF = F - i
        if (newC % newF == 0):
            best1 = i
            break

    best2 = float('inf')
    for i in range(C):
        newC = C - i
        newF = F + i
        if (newF > newC):
            break
        if (newC % newF == 0):
            best2 = i
            break

    print(min(best1, best2))
