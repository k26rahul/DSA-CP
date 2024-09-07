N, M = map(int, input().split())

adj_list = {u: [] for u in range(1, N+1)}

for _ in range(M):
  A, B = map(int, input().split())
  adj_list[A].append(B)
  adj_list[B].append(A)

parent = list(range(N+1))
rank = [0] * (N+1)


def find(x):
  if parent[x] != x:
    parent[x] = find(parent[x])
  return parent[x]


def union(x, y):
  x_root, y_root = find(x), find(y)
  if x_root == y_root:
    return
  if rank[x_root] < rank[y_root]:
    parent[x_root] = y_root
  elif rank[x_root] > rank[y_root]:
    parent[y_root] = x_root
  else:
    parent[y_root] = x_root
    rank[x_root] += 1


for u in adj_list:
  for v in adj_list[u]:
    union(u, v)

num_components = sum(1 for i in range(1, N+1) if parent[i] == i)
print(num_components - 1)

# N, M = map(int, input().split())

# adj_list = {u: [] for u in range(1, N+1)}

# for _ in range(M):
#   A, B = map(int, input().split())
#   adj_list[A].append(B)
#   adj_list[B].append(A)


# def bfs(adj_list, start, visited):
#   component = []
#   queue = [start]

#   while queue:
#     u = queue.pop(0)
#     if not visited[u]:
#       visited[u] = True
#       component.append(u)

#       for v in adj_list[u]:
#         if not visited[v]:
#           queue.append(v)
#   return component


# visited = {u: False for u in adj_list}
# components = []

# for u in adj_list:
#   if not visited[u]:
#     component = bfs(adj_list, u, visited)  # helper
#     components.append(component)
# print(len(components)-1)
