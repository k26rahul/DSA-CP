n, k = map(int, input().split())

half = int(n/2 if n % 2 == 0 else n/2 + 1)

if k > half:
    k = k - half
    print(2*k)
else:
    print(2*k - 1)
