T = int(input())  # total test cases

# loop over all test cases
for _ in range(T):
  # handle each test case here
  x, y = list(map(int, input().split()))
  if x < y:
    print(f'{x} {y}')
  else:
    print(f'{y} {x}')
