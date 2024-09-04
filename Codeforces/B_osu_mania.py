T = int(input())

for _ in range(T):
  # solve each test case here
  n = int(input())
  cols = []
  for _ in range(n):
    for i, char in enumerate(input()):
      if char == '#':
        cols.append(str(i+1))
  print(' '.join(cols[::-1]))
