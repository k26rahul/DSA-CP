n = int(input())
problems = []

for i in range(n):
    problems.append(1 if sum(map(int, input().split())) >= 2 else 0)

print(sum(problems))
