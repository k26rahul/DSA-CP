s = input()

hello_found = False
h_found, e_found, l1_found, l2_found, o_found = [False] * 5

for char in s:
    if char == 'h':
        h_found = True
        continue

    if char == 'e' and h_found:
        e_found = True
        continue

    if char == 'l' and h_found and e_found and not l1_found:
        l1_found = True
        continue

    if char == 'l' and h_found and e_found and l1_found:
        l2_found = True
        continue

    if char == 'o' and h_found and e_found and l1_found and l2_found:
        hello_found = True
        break


print('YES' if hello_found else 'NO')
