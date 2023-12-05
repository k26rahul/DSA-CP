from string import ascii_lowercase, ascii_uppercase

T = int(input())

for _ in range(T):
  word = input()
  n = len(word)

  final = ''
  i_last_up = None
  i_last_low = None

  for letter in word:
    if letter == 'b':
      if i_last_low:
        final = final[:i_last_low] + final[i_last_low+1:]

    elif letter == 'B':
      if i_last_up:
        final = final[:i_last_up] + final[i_last_up+1:]

    elif letter in ascii_lowercase:
      final += letter
      i_last_low = len(final) - 1

    elif letter in ascii_uppercase:
      final += letter
      i_last_up = len(final) - 1

  print(word)
