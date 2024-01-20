T = int(input())

for _ in range(T):
  n = int(input())
  a = input()
  b = input()
  c = input()

  exists = False
  for i in range(n):
    if len(set([a[i], b[i], c[i]])) == 3:
      exists = True

  print('YES' if exists else 'NO')
