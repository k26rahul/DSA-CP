n = int(input())

BB = 0
CC = 0
BC = []
CB = []

for i in range(n):
    d = input()

    if d[0] == d[-1] == 'B':
        BB += len(d)
    elif d[0] == d[-1] == 'C':
        CC += len(d)
    elif d[0] == 'B' and d[-1] == 'C':
        BC.append(d)
    else:
        CB.append(d)

BC.sort(key=lambda d: len(d), reverse=True)
CB.sort(key=lambda d: len(d), reverse=True)

if len(BC) == len(CB) == 0:
    print(max([BB, CC]))
else:
    if len(BC) > len(CB):
        BC, CB = CB, BC
    print(len(
        ''.join(
            [*BC, *CB[:len(BC) + 1]]
        )
    ) + BB + CC)
