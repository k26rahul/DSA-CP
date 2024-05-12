T = int(input())

for _ in range(T):
  n, m, k = list(map(int, input().split()))
  b_list = list(map(int, input().split()))
  c_list = list(map(int, input().split()))

  count = 0
  for b in b_list:
    for c in c_list:
      if b+c <= k:
        count += 1

  print(count)
