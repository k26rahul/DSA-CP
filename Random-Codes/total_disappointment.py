m, n = map(int, input().split())

total_demand = 0
for i in range(n):
    total_demand += int(input())

total_disappointment = m - total_demand

base = total_disappointment // n
excess = total_disappointment % n

ans = (base ** 2) * (n - excess)
ans += ((base + 1) ** 2) * excess

print(ans)
