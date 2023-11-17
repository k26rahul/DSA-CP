n = int(input())

vectors = []

for i in range(n):
    vectors.append(map(int, input().split()))

is_in_equilibrium = all(x == 0 for x in [sum(k) for k in list(zip(*vectors))])

print('YES' if is_in_equilibrium else 'NO')
