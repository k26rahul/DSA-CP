n = int(input())
proportions = map(int, input().split())

print(sum([1 * p/100 for p in proportions])/n * 100)
