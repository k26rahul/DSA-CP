T = int(input())

for _ in range(T):
  spent = [0] * 27
  solved = 0

  n = int(input())
  log = input()

  for letter in log:
    index = ord(letter) - 65 + 1

    spent[index] += 1

    if spent[index] == index:
      solved += 1

  print(solved)
