T = int(input())

for _ in range(T):
  # solve each test case here
  points = set()
  freq_y0 = 0
  freq_y1 = 0
  freq_x1 = 0
  n = int(input())
  for _ in range(n):
    x, y = map(int, input().split())
    points.add((x, y))
    if y == 0:
      freq_y0 += 1
    else:
      freq_y1 += 1
      freq_x1 += 1

  ans = 0
  if freq_y1 == 0 or freq_y0 == 0:
    print(ans)
    continue

  for x, y in points:
    if y == 1:
      if (x, 0) in points:
        ans += freq_y0-1
        ans += freq_x1-1
      if (x-1, 0) in points and (x+1, 0) in points:
        ans += 1
    else:
      if (x-1, 1) in points and (x+1, 1) in points:
        ans += 1
  print(ans)
