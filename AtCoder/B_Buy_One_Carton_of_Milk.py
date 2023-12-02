# import math

# n, s, m, l = map(int, input().split())
# #  6, 8, 12


# def calc(n):
#     return min(
#         math.ceil(n / 6) * s,
#         math.ceil(n / 8) * m,
#         math.ceil(n / 12) * l,
#     )


# print(min(
#     (n // 6) * s + calc(n % 6),
#     (n // 8) * m + calc(n % 8),
#     (n // 12) * l + calc(n % 12),
# ))

# print(
#     [n, n % 6, calc(n % 6)],
#     [n, n % 8, calc(n % 8)],
#     [n, n % 12, calc(n % 12)],
# )

# # print(
# #     math.ceil(n / 6),
# #     math.ceil(n / 8),
# #     math.ceil(n / 12),
# # )

# # print(
# #     math.ceil(n / 6) * s,
# #     math.ceil(n / 8) * m,
# #     math.ceil(n / 12) * l,
# # )


# # pricing = sorted([(6, s/6), (8, m/8), (12, l/12)], key=lambda pair: pair[1])
# # print(pricing)

# # q, p = pricing[0]
# # rem = n % q
# # money0 = ((n - rem) / q) * s

# # q, p = pricing[1]
# # rem = n % q
# # money1 = ((n - rem) / q) * m

# # q, p = pricing[2]
# # rem = n % q
# # money2 = ((n - rem) / q) * l

# # print(money0, money1, money2)

ans = None
# for x in range(5):
#     for y in range(5):
#         if 3 ** x + 4 ** y == 31 and 3 ** (x+1) + 4 ** (y+1) == 97:
#             ans = x, y
#             break

# print(ans)

for p in range(100):
    for q in range(100):
        for r in range(100):
            if (p * (6 ** 0.5) + q + r * (3 ** 0.5))/8 == (3 ** .5) / ((2 ** .5) + 2 * (6 ** .5)):
                ans = p, q, r

print(ans)
