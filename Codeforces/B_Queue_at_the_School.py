n, t = map(int, input().split())
children = input()

for _ in range(t):
    new_children = ''
    i = 0
    while i < n:
        if children[i:i+2] == 'BG':
            new_children += 'GB'
            i += 1
        else:
            new_children += children[i]
        i += 1

    children = new_children

print(children)
