T = int(input())

for _ in range(T):
  n, k = map(int, input().split())
  b = list(map(int, input().split()))

  ok = True
  product = 1
  for num in b:
    if num not in {1, 7, 17, 119, 289, 2023}:
      print('NO')
      ok = False
      break

    product *= num
    if product not in {1, 7, 17, 119, 289, 2023}:
      print('NO')
      ok = False
      break

  if ok:
    print('YES')
    print(2023//product, *([1] * (k-1)))
    # if product == 2023:
    #   print('YES')
    #   print(*([1] * k))
    # if product == 289:
    #   print('YES')
    #   print(7, *([1] * (k-1)))
    # if product == 119:
    #   print('YES')
    #   print(17, *([1] * (k-1)))
    # if product == 17:
    #   print('YES')
    #   print(119, *([1] * (k-1)))
    # if product == 7:
    #   print('YES')
    #   print(289, *([1] * (k-1)))
    # if product == 1:
    #   if k >= 3:
    #     print('YES')
    #     print(7, 17, 17, *([1] * (k-3)))
    #   else:
    #     print('NO')
