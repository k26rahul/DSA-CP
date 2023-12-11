T = int(input())

for _ in range(T):
  n, k = map(int, input().split())

  half_n = n // 2
  half_half_n = half_n // 2

  if n % 2 == 1:
    print(f'1 {half_n} {half_n}')

  elif half_n % 2 == 0:
    print(f'{half_n} {half_half_n} {half_half_n}')

  else:
    print(f'2 {half_n - 1} {half_n - 1}')
