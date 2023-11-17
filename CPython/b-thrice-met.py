# https://cpython.uz/competitions/contests/contest/288/problems

input()
arr = input().split(' ')

c = [0 for _ in range(10)]
o = []
for x in arr:
    ix = int(x)

    c[ix] += 1

    if c[ix] == 3:
        o.append(x)
        c[ix] = 0

print(' '.join(o))
