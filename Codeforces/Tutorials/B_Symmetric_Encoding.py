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
  decoded = ''
  for letter in input_string:
    new_letter = encoding_map[letter]
    decoded += new_letter

  print(decoded)
