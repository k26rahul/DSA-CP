# https://www.spoj.com/problems/HC/

for _ in range(int(input())):
    coins = [input() for _ in range(
        int(input())
    )]

    nosLxh = coins.count('lxh')

    if nosLxh % 2 == 0:
        print('hhb')
    else:
        print('lxh')
