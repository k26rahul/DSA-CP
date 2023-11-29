import math

T = int(input())

for _ in range(T):
    N, B, K = map(int, input().split())

    G = N - B

    BK = B % K
    GK = G % K

    print(abs(BK - GK))
