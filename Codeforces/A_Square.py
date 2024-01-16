T = int(input())

for _ in range(T):
  ax, ay = map(int, input().split())
  bx, by = map(int, input().split())
  cx, cy = map(int, input().split())
  dx, dy = map(int, input().split())

  x1, x2 = list(set([ax, bx, cx, dx]))
  y1, y2 = list(set([ay, by, cy, dy]))

  print(abs(x1 - x2) * abs((y1 - y2)))
