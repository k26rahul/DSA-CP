T = int(input())

for _ in range(T):
  word = input()
  n = len(word)

  count_B = 0
  count_b = 0
  final = ''

  for letter in reversed(word):
    if letter == 'b':
      count_b += 1
    elif letter == 'B':
      count_B += 1

    elif letter.isupper():
      if count_B:
        count_B -= 1
      else:
        final += letter

    elif letter.islower():
      if count_b:
        count_b -= 1
      else:
        final += letter

  print(''.join(list(reversed(final))))
