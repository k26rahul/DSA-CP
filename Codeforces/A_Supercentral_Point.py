n = int(input())
points = []

for _ in range(n):
    points.append(list(map(int, input().split())))

supercentral = 0
for i in range(n):
    x, y = points[i]

    right_neighbor = False
    left_neighbor = False
    lower_neighbor = False
    upper_neighbor = False

    for x2, y2 in points:
        if x2 == x:
            if y2 > y:
                upper_neighbor = True
            if y2 < y:
                lower_neighbor = True

        if y2 == y:
            if x2 > x:
                right_neighbor = True
            if x2 < x:
                left_neighbor = True

    if right_neighbor and left_neighbor and lower_neighbor and upper_neighbor:
        supercentral += 1

print(supercentral)
