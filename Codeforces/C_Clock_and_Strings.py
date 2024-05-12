T = int(input())

for _ in range(T):
  a, b, c, d = list(map(int, input().split()))
  clock = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
  group1 = []
  group2 = []

  where_to_put = 1
  for number in clock:
    if number == a or number == b:
      if where_to_put == 1:
        where_to_put = 2
      else:
        where_to_put = 1
      continue

    if where_to_put == 1:
      group1.append(number)
    else:
      group2.append(number)

  if c in group1 and d in group2:
    print('YES')
  elif d in group1 and c in group2:
    print('YES')
  else:
    print('NO')
