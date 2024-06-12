T = int(input())


def check_good(prefix):
  prefix_sum = sum(prefix)
  for x in prefix:
    if prefix_sum - x == x:
      return True
  return False


for _ in range(T):
  n = int(input())
  array = list(map(int, input().split()))

  ans = 0
  for i in range(n):
    prefix = array[:i+1]
    if check_good(prefix):
      ans += 1

  print(ans)
