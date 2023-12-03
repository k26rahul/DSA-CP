n = int(input())
a_list = map(int, input().split())
m = int(input())
b_list = map(int, input().split())

index = {}

l_comparisons = 0
r_comparisons = 0

for i, a in enumerate(a_list, 1):
    index[a] = i

for b in b_list:
    i = index[b]
    l_comparisons += (i)
    r_comparisons += (n - i + 1)

print(l_comparisons, r_comparisons)
# print(index)
