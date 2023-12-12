# num = input()

# is_magic_number = True
# for digit in num:
#   if digit not in {'1', '4'}:
#     is_magic_number = False
#     break

# print('YES' if is_magic_number else 'NO')

num = input()
n = len(num)

is_magic_number = True

i = 0
while i < n:
  if num[i:i+3] == '144':
    i += 3
    continue
  if num[i:i+2] == '14':
    i += 2
    continue
  if num[i] == '1':
    i += 1
    continue
  is_magic_number = False
  break

print('YES' if is_magic_number else 'NO')
