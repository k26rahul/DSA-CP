T = int(input())

for _ in range(T):
  n = int(input())
  s1 = input()
  s2 = input()
  s2_1 = 0
  s2_0 = 0
  for i in range(n):
    if s1[i] == s2[i]:
      continue
    if s2[i] == '1':
      s2_1 += 1
    if s2[i] == '0':
      s2_0 += 1

  print()
