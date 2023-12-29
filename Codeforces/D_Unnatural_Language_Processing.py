T = int(input())

C = {'b', 'c', 'd'}
V = {'a', 'e'}

for _ in range(T):
  n = int(input())
  s = input()

  syllables = []

  i = 1
  part = s[0]
  last = s[0]
  while i < n:
    curr = s[i]

    part += curr
    if len(part) == 2:
      if part[0] in C and part[1] in C:
        syllables[-1] += part[0]
        part = part[-1]
      else:
        syllables.append(part)
        part = ''

    i += 1

  if part and len(part) == 1:
    syllables[-1] += part
  elif part:
    syllables.append(part)
  print('.'.join(syllables))
