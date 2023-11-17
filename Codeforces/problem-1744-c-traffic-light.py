# https://codeforces.com/problemset/problem/1744/C

T = int(input())

for _ in range(T):
    n, c = input().split(' ')
    n = int(n)
    s = input() * 2

    if c == 'g':
        print(0)
        continue

    i = 1
    ic = 1
    flag = True
    time = 0
    for char in s:
        if not flag and char == 'g':
            flag = True
            time = max(time, i - ic)
        elif flag and char == c and i <= n:
            ic = i
            flag = False
        i += 1

    print(time)
