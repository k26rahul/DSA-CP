n, k, l, c, d, p, nl, np = map(int, input().split())

drink_milliliters = k * l
lime_slices = c * d

toast1 = drink_milliliters // nl
toast2 = lime_slices
toast3 = p // np

print(min(toast1, toast2, toast3)//n)
