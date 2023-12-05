a, b, c = map(int, input().split())

x = int((a * b / c) ** 0.5)
y = int((b * c / a) ** 0.5)
z = int((c * a / b) ** 0.5)

print(4 * (x + y + z))
