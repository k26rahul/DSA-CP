T = int(input())

for _ in range(T):
  input_str = input()
  uppercase = []
  lowercase = []

  for i in range(len(input_str)):
    if input_str[i] == 'B':
      if uppercase:
        uppercase.pop()

    elif input_str[i] == 'b':
      if lowercase:
        lowercase.pop()

    elif 'a' <= input_str[i] <= 'z':
      lowercase.append(i)

    elif 'A' <= input_str[i] <= 'Z':
      uppercase.append(i)

  combine = uppercase + lowercase
  combine.sort()

  ans = ''.join(input_str[x] for x in combine)
  print(ans)
