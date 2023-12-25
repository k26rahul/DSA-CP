a, b, n = map(int, input().split())

found = False
for digit in range(10):
  if (a * 10 + digit) % b == 0:
    found = True
    print(str(a * 10 + digit) + '0' * (n - 1))
    break

if not found:
  print(-1)
