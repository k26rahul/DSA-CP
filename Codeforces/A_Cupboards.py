n = int(input())
cupboards = []

for i in range(n):
    cupboards.append(list(map(int, input().split())))

l = [c[0] for c in cupboards]
r = [c[1] for c in cupboards]


sum_l = sum(l)
sum_r = sum(r)

print(min(n - sum_l, sum_l) + min(n - sum_r, sum_r))

# print(n - max(sum_l, sum_r) + min(sum_l, sum_r))
