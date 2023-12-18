T = int(input())

for _ in range(T):
  ab = input()

  a = ''
  for i in range(len(ab)):
    if i == 0:
      a += ab[i]
      continue
    if ab[i] == '0':
      a += ab[i]
    else:
      break

  b = ab[len(a):]

  if b != '' and int(b) > int(a):
    print(a, b, sep=' ')
  else:
    print(-1)
