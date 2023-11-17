for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print('0 0')

    elif abs(a - b) == 1:
        print('1 0')

    else:
        gcd = abs(a - b)
        x = b % gcd
        steps = 0 if x == 0 else min(x, gcd-x)
        print(f'{gcd} {steps}')
