T = int(input())

for _ in range(T):
  n = int(input())
  nums = input().split()

  total_neg = 0
  zero = False

  for i in range(n):
    num = int(nums[i])

    if num == 0:
      zero = True

    if num < 0:
      total_neg += 1

  if zero or (total_neg & 1):
    print(0)
  else:
    print(1)
    print(1, 0)
