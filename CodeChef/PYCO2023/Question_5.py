nums = [int(input()) for _ in range(int(input()))]

print(sum(x for x in nums if not x & 1))
print(sum(x for x in nums if x & 1))
