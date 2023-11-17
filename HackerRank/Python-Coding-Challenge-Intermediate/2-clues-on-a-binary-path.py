# hackerrank.com/contests/python-coding-challenge-1694856413/

def cluesOnBinaryPath(n, d, roads):
    graph = [[] for _ in range(n)]

    for u, v, c in roads:
        graph[u - 1].append((v, c))
        graph[v - 1].append((u, c))

    def dfs(node, length, binary_seq):
        if length == d:
            return 1

        count = 0
        for neighbor, weight in graph[node - 1]:
            new_binary_seq = binary_seq + str(weight)
            count += dfs(neighbor, length + 1, new_binary_seq)

        return count

    total_paths = 0
    for neighbor, weight in graph[0]:
        binary_seq = str(weight)
        total_paths += dfs(neighbor, 1, binary_seq)

    return total_paths


print(cluesOnBinaryPath(3, 3, [
    [1, 2, 0],
    [1, 3, 1],
]))
