n, m = map(int, input().split())
children = list(
    zip(range(1, n + 1), map(int, input().split()))
)

last = None
while len(children) > 0:
    new_children = []
    for child in children:
        i, wants = child
        last = i
        if wants > m:
            new_children.append((i, wants - m))

    children = new_children

print(last)
