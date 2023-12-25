import sys

# Set the maximum number of digits for integer string conversion
sys.set_int_max_str_digits(100000)

a, b, n = map(int, input().split())
given_a = a

for _ in range(n):
  old_a = a

  for i in range(10):
    new_a = int(str(a) + str(i))
    if new_a % b == 0:
      a = new_a
      break

  if a == old_a:
    break

print(-1 if given_a == a else a)
