# https://www.spoj.com/problems/HC/

numberOfTestCases = int(input())


def solve():
    numberOfCoins = int(input())

    coins = []
    for _ in range(numberOfCoins):
        coins.append(input())

    nosLxh = coins.count('lxh')
    isNosLxhEven = nosLxh % 2 == 0

    nosHhb = coins.count('hhb')
    isNosHhbEven = nosHhb % 2 == 0

    if nosHhb == 0:
        print('hhb' if isNosLxhEven else 'lxh')

    elif nosLxh == 0:
        print('hhb')

    elif isNosLxhEven and isNosHhbEven:
        print('hhb')

    elif not isNosLxhEven and not isNosHhbEven:
        print('lxh')

    else:
        print('hhb' if isNosLxhEven else 'lxh')


for _ in range(numberOfTestCases):
    solve()
