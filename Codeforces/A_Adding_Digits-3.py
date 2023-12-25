a, b, n = map(int, '100000 10 64479'.split())

ans = str(a)


def find_next_digit():
  for digit in range(10):
    if (a * 10 + digit) % b == 0:
      return digit
  return -1


for _ in range(n):
  digit = find_next_digit()

  if digit == -1:
    print(-1)
    break

  a = a * 10 + digit
  ans += str(digit)
else:
  print(ans)
