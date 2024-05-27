import math

T = int(input())  # total test cases

for _ in range(T):
  # handle each test cases here
  x, y = map(int, input().split())

  screens_needed = math.ceil(y/2)
  cells_used = y * 4
  cell_unused = (screens_needed * 15) - cells_used

  if cell_unused >= x:  # do we have enough empty cells for 1x1?
    print(screens_needed)
    continue  # skip to next test case

  # otherwise we add more screens
  x -= cell_unused  # use all empty cells, and be left with some 1x1 icons
  additional_screens = math.ceil(x/15)
  print(screens_needed + additional_screens)
