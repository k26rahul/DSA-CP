import math

T = int(input())

for _ in range(T):
  # solve each test case here
  x, y, k = map(int, input().split())
  x_steps = math.ceil(x/k)
  y_steps = math.ceil(y/k)

  # approach 1: x > y in base formula
  clip = 1
  if x < y or x_steps == y_steps:
    clip = 0
  print(x_steps + y_steps + abs(x_steps-y_steps) - clip)

  # # approach 2: y > x in base formula
  # clip = 0
  # if y < x and x_steps != y_steps:
  #   clip = 1
  # print(x_steps + y_steps + abs(x_steps-y_steps) - clip)
