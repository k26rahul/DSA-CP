# Find out how many people Robin gives gold to.

T = int(input())

for _ in range(T):
  n, k = map(int, input().split())  # unpack
  people = list(map(int, input().split()))  # NO unpack, so we do list()
  wallet = 0
  count = 0
  for gold in people:
    if gold >= k:
      wallet += gold  # steal all gold
    elif gold == 0 and wallet > 0:
      wallet -= 1  # give 1 gold
      count += 1

  print(count)
