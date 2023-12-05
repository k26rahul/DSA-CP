n = int(input())
heights = list(map(int, input().split()))

heights = [heights[-1]] + heights
min_height = 1000
recon_pairs = None
for i in range(n):
    h = abs(heights[i] - heights[i + 1])
    if h < min_height:
        min_height = h
        recon_pairs = i, i + 1

a = recon_pairs[0]
b = recon_pairs[1]
a = n if a == 0 else a

print(a, b)
