T = int(input())

for _ in range(T):
  k = list(map(int, input().split()))
  if k[0] == k[1]:
    print(k[2])
  if k[1] == k[2]:
    print(k[0])
  if k[0] == k[2]:
    print(k[1])
