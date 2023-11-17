# https://codeforces.com/problemset/problem/1195/B

n, k = [int(i) for i in input().split(' ')]

low = 0
high = n - 1
candiesAte = 0
while low <= high:
    candiesAte = (low + high) // 2

    candiesPut = ((n - candiesAte) * (n - candiesAte + 1)) / 2
    candiesAtEnd = candiesPut - candiesAte

    if candiesAtEnd == k:
        break
    elif candiesAtEnd < k:
        high = candiesAte - 1
    else:
        low = candiesAte + 1

print(candiesAte)
