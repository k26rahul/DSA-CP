# https://codeforces.com/problemset/problem/1095/B

n = int(input())
a = [int(x) for x in input().split(' ')]

a1 = a[:]
a1.remove(max(a1))
instability_a1 = max(a1) - min(a1)

a2 = a[:]
a2.remove(min(a2))
instability_a2 = max(a2) - min(a2)

print(min([instability_a1, instability_a2]))
