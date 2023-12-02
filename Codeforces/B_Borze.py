code = input()
number = ''

i = 0
while i < len(code):
    if code[i] == '.':
        number += '0'
        i += 1
        continue

    block = code[i:i+2]
    if block == '-.':
        number += '1'
    elif block == '--':
        number += '2'
    elif block == '..':
        number += '00'
    i += 2

print(number)
