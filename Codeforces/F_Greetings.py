T = int(input())

for _ in range(T):
  n = int(input())
  k = sorted([tuple(map(int, input().split()))
             for _ in range(n)], key=lambda tup: tup[1], reverse=True)

  greetings = 0
  for i in range(n):
    left, right = k[i]
    for j in range(i + 1, n):
      left2, right2 = k[j]
      if left < right2:
        if right2 - left >= right2 - left2:
          greetings += 1
      else:
        break

  print(greetings)
  # print(k)
