T = int(input())

for _ in range(T):
  for _ in range(3):
    k = input()
    if '?' in k:
      target = k

  if 'A' in target and 'B' in target:
    print('C')
    continue
  if 'B' in target and 'C' in target:
    print('A')
    continue
  if 'A' in target and 'C' in target:
    print('B')
    continue
