T = int(input())

for _ in range(T):
  n = int(input())

  miners, mines = [], []

  for _ in range(2 * n):
    x, y = map(int, input().split())

    if x == 0:
      miners.append(abs(y))
    if y == 0:
      mines.append(abs(x))

  miners.sort()
  mines.sort()
  print(sum([(a**2 + b**2) ** .5 for a, b in zip(miners, mines)]))
