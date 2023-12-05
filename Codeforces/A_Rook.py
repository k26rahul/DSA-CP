T = int(input())

letter_to_num = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
}

num_to_letter = {
    1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'
}

for _ in range(T):
  column, row = list(input())
  column = letter_to_num[column]
  row = int(row)

  print(column, row)

  for r in range(1, 9):
    if r == row:
      continue
    print(num_to_letter[column] + str(r))

  for c in range(1, 9):
    if c == column:
      continue
    print(num_to_letter[c] + str(row))
