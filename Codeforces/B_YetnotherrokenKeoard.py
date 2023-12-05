from string import ascii_lowercase, ascii_uppercase

T = int(input())

for _ in range(T):
  word = input()
  n = len(word)

  i_last_up = []
  i_last_low = []
  mask = [True] * n

  for i in range(n):
    letter = word[i]

    if letter == 'b':
      mask[i] = False
      if i_last_low:
        mask[i_last_low[-1]] = False
        i_last_low = i_last_low[:-1]

    elif letter == 'B':
      mask[i] = False
      if i_last_up:
        mask[i_last_up[-1]] = False
        i_last_up = i_last_up[:-1]

    elif letter in ascii_lowercase:
      i_last_low.append(i)

    elif letter in ascii_uppercase:
      i_last_up.append(i)

  # print(mask)

  final = ''
  for i, char in enumerate(word):
    if mask[i]:
      final += char

  print(final)
