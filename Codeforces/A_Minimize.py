T = int(input())

for _ in range(T):
  # solve each test case here
  a, b = map(int, input().split())
  print(min(c - a + b - c for c in range(a, b+1)))
