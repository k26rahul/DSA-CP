# https://cpython.uz/competitions/contests/contest/288/problems

str1 = set(input())
str2 = set(input())

diff = ''.join(sorted(
    list(str1 - str2)
))

print(diff or 'Empty')
