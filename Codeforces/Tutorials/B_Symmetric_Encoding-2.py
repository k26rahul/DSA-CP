T = int(input())

for _ in range(T):
  input()  # discard the 1st line of each test case
  input_string = input()

  # auxiliary string (we make a list instead)
  distinct_sorted_letters = sorted(list(set(input_string)))

  # make encoding map
  encoding_map = {}
  n = len(distinct_sorted_letters)
  for i in range(n):
    key = distinct_sorted_letters[i]
    value = distinct_sorted_letters[n-1-i]
    encoding_map[key] = value

  # do decoding
  decoded = [0] * len(input_string)
  for i in range(len(input_string)):
    decoded[i] = encoding_map[input_string[i]]

  print(''.join(decoded))
