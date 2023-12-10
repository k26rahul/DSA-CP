T = int(input())

for _ in range(T):
  word = input()
  n = len(word)

  count_B = 0
  count_b = 0
  final = ''

  for i in range(n - 1, -1, -1):
    letter = word[i]

    if letter == 'b':
      count_b += 1
    elif letter == 'B':
      count_B += 1

    elif 'A' <= letter <= 'Z':
      if count_B:
        count_B -= 1
      else:
        final = letter + final

    else:
      if count_b:
        count_b -= 1
      else:
        final = letter + final

  print(final)
