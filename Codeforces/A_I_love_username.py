n = int(input())
performances = list(map(int, input().split()))

best = performances[0]
worst = performances[0]
amazing = 0
for i in range(1, n):
    if performances[i] > best:
        amazing += 1
        best = performances[i]

    elif performances[i] < worst:
        amazing += 1
        worst = performances[i]


print(amazing)
