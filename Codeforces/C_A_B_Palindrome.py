T = int(input())

for _ in range(T):
  a, b = map(int, input().split())
  string = list(input())

  n = a + b
  count0, count1 = 0, 0
  dual_q_mark = 0
  extra_q = False

  for i in range(n // 2):
    l = string[i]
    r = string[n - i - 1]

    if l == r == '0':
      count0 += 2
      continue
    if l == r == '1':
      count1 += 2
      continue

    if l != '?' and r != '?' and l != r:
      print(-1)
      break

    if l == '?' and r == '?':
      # dual_q_mark += 1
      if (count0 + 2) <= a:
        string[i] = '0'
        string[n - i - 1] = '0'
        count0 += 2
      if (count1 + 2) <= b:
        string[i] = '1'
        string[n - i - 1] = '1'
        count1 += 2
      continue
    if l == '?' and r == '0':
      string[i] = r
      count0 += 2
    if l == '?' and r == '1':
      string[i] = r
      count1 += 2

    if r == '?' and l == '?':
      # dual_q_mark += 1
      if (count0 + 2) <= a:
        string[i] = '0'
        string[n - i - 1] = '0'
        count0 += 2
      if (count1 + 2) <= b:
        string[i] = '1'
        string[n - i - 1] = '1'
        count1 += 2
      continue
    if r == '?' and l == '0':
      string[n - i - 1] = l
      count0 += 2
    if r == '?' and l == '1':
      string[n - i - 1] = l
      count1 += 2

  if n % 2 == 1:
    if string[n//2] == '0':
      count0 += 1
    elif string[n//2] == '1':
      count1 += 1
    else:
      extra_q = True

  print(a, b)
  print(count0, count1, dual_q_mark)
  print(''.join(string))
