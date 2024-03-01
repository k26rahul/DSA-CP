T = int(input())

for _ in range(T):
  n = int(input())
  a = list(map(int, input().split()))

  sum_a = 0
  found_mod_1 = False
  found_mod_2 = False
  for x in a:
    if x % 3 == 1:
      found_mod_1 = True
    if x % 3 == 2:
      found_mod_2 = True
    sum_a += x

  print(f'{a=}, {sum_a=}, %3={sum_a % 3}')

  # if sum_a % 3 == 0:
  #   print(0)
  # elif sum_a % 3 == 1:
  #   print(1 if found_mod_1 else 2)
  # else:
  #   print(1 if found_mod_1 or found_mod_2 else 2)
