T = int(input())

for _ in range(T):
  n = int(input())
  a = list(map(int, input().split()))

  ans = [(a[0], a[0])] * n

  i = 0
  for num in a:
    if i == 0:
      i += 1
      continue

    down, ok = ans[i-1]

    new_ok = ok + num
    new_down = new_ok
    if new_ok & 1 or (down + num) & 1:
      new_down -= 1

    ans[i] = (new_down, new_ok)
    i += 1

  print(*[a[0] for a in ans])
