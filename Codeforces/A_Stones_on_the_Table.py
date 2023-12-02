n = int(input())
stones = input()

take = 0
i = 0
while i < n:
    if i+1 < n and stones[i] == stones[i+1]:
        take += 1
    i += 1

print(take)
