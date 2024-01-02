import math


def get_lcm(a, b):
  return abs(a * b) // math.gcd(a, b)


T = int(input())

for _ in range(T):
  a, b = map(int, input().split())

  if a == b:
    print(a * b)
    break

  lcm = get_lcm(a, b)
  if lcm == b:
    lcm *= lcm / a

  print(int(lcm))
