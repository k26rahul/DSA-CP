T = int(input())

for _ in range(T):
  n = int(input())
  print(sum(abs(int(x)) for x in input().split()))
