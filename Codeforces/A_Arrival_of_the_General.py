n = int(input())
line = list(map(int, input().split()))

imax = line.index(max(line))
imin_reversed = list(reversed(line)).index(min(line))
imin = n - 1 - imin_reversed

if imin > imax:
    print(imax + imin_reversed)
else:
    print(imax + imin_reversed - 1)

# print(imax, imin)
