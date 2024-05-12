T = int(input())

for _ in range(T):
  n = int(input())
  s = input()
  rev_s = s[::-1]
  if s == rev_s:
    print(s)
  elif s < rev_s:
    print(s)
  else:
    print(rev_s + s)
