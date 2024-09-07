N = int(input())

adj_list = {u: [] for u in range(1, N+1)}

for _ in range(N-1):
  A, B = map(int, input().split())
  adj_list[A].append(B)
  adj_list[B].append(A)

visited = {u: False for u in adj_list}
stack = [1]
order = []

while stack:
  u = stack.pop()
  order.append(str(u))
  if not visited[u]:
    visited[u] = True
    for v in sorted(reversed(adj_list[u])):
      if not visited[v]:
        stack.append(u)
        stack.append(v)

print(' '.join(reversed(order)))
