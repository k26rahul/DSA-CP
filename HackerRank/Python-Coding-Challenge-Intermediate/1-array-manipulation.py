# hackerrank.com/contests/python-coding-challenge-1694856413/

def arrayManipulation(n, queries):
    L = [0] * (n + 1)

    for q in queries:
        a, b, k = q
        L[a - 1] += k
        L[b] -= k

    current = 0
    max_value = 0
    for value in L:
        current += value
        max_value = max(max_value, current)

    return max_value


print(arrayManipulation(10, [
    [1, 5, 3],
    [4, 8, 7],
    [6, 9, 1],
]))


print(arrayManipulation(5, [
    [1, 2, 100],
    [2, 5, 100],
    [3, 4, 100],
]))
