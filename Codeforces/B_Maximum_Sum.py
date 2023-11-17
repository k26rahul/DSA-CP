for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(
        map(int, input().split())
    )

    for _ in range(k):
        a = a[2:] if (a[0]+a[1]) < a[-1] else a[:-1]

    print(sum(a))
