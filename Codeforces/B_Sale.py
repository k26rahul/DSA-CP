n, m = map(int, input().split())
prices = sorted(map(int, input().split()))

total = 0
i = 0
while i < m:
  if prices[i] < 0:
    total += prices[i]
  else:
    break
  i += 1

print(abs(total))
