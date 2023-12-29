T = int(input())

for _ in range(T):
  n = int(input())
  k = sum(map(int, input().split()))

  sqrt = k ** .5
  print('YES' if sqrt // 1 == sqrt else 'NO')
