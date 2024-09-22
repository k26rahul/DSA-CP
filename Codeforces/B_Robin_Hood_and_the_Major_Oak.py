T = int(input())

for _ in range(T):
  n, k = map(int, input().split())  # unpack

  # ~ 6E 6O : nos_even, nos_odd
  nos_even = 0
  nos_odd = 0
  if n % 2 == 0:
    if k % 2 == 0:
      nos_even = k//2
      nos_odd = k//2
    else:
      nos_even = k//2+1
      nos_odd = k//2
  else:
    if k % 2 == 0:
      nos_even = k//2
      nos_odd = k//2
    else:
      nos_even = k//2
      nos_odd = k//2+1

  # print(f'{nos_even} {nos_odd}')
  # ~ nos_even, nos_odd - -> E/O
  if nos_even % 2 == 0 and nos_odd % 2 == 0:
    print('YES')
  elif nos_even % 2 == 0 and nos_odd % 2 == 1:
    print('NO')
  elif nos_even % 2 == 1 and nos_odd % 2 == 0:
    print('YES')
  elif nos_even % 2 == 1 and nos_odd % 2 == 1:
    print('NO')
