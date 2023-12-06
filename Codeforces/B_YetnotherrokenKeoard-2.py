from string import ascii_lowercase, ascii_uppercase

T = int(input())

for _ in range(T):
  word = input()
  n = len(word)

  final = ''
  i_last_up = []
  i_last_low = []

  for letter in word:
    if letter == 'b':
      if i_last_low:
        i = i_last_low.pop()
        final = final[:i] + final[i+1:]
        i_last_up = [k - 1 if k > i else k for k in i_last_up]
        i_last_low = [k - 1 if k > i else k for k in i_last_low]

    elif letter == 'B':
      if i_last_up:
        i = i_last_up.pop()
        final = final[:i] + final[i+1:]
        i_last_up = [k - 1 if k > i else k for k in i_last_up]
        i_last_low = [k - 1 if k > i else k for k in i_last_low]

    elif letter in ascii_lowercase:
      final += letter
      i_last_low.append(len(final) - 1)

    elif letter in ascii_uppercase:
      final += letter
      i_last_up.append(len(final) - 1)

  print(final)
