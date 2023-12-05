T = int(input())

for _ in range(T):
  n = int(input())
  s = input()

  i = 1
  while i < len(s):
    if s[i] == s[i - 1]:
      i += 1
      continue
    else:
      s = s[:i - 1] + s[i + 1:]
      i -= 1
    i += 1

    if i > len(s):
      i -= 1

  print(s)
