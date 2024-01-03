s = input().lower()
print(sum(s.count(v) for v in {'a', 'e', 'i', 'o', 'u'}))
