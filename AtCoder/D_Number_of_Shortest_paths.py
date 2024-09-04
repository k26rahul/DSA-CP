# import heapq


# class PriorityQueue:
#   def __init__(self):
#     self.heap = []

#   def is_empty(self):
#     return len(self.heap) == 0

#   def enqueue(self, priority, item):
#     heapq.heappush(self.heap, (priority, item))

#   def dequeue(self):
#     return heapq.heappop(self.heap)[1]


# def dijkstra(adj_list, start_vertex):
#   # Dijkstra's Algorithm (slightly modified for `predecessor`)
#   visited = {u: False for u in adj_list}
#   predecessor = {u: [] for u in adj_list}
#   distance = {u: float('inf') for u in adj_list}
#   distance[start_vertex] = 0

#   pq = PriorityQueue()
#   pq.enqueue(0, start_vertex)

#   while not pq.is_empty():
#     u = pq.dequeue()
#     visited[u] = True

#     for v in adj_list[u]:
#       if not visited[v]:
#         new_distance = distance[u] + 1
#         if new_distance < distance[v]:
#           distance[v] = new_distance
#           pq.enqueue(new_distance, v)
#           predecessor[v] = [u]
#         elif new_distance == distance[v]:
#           predecessor[v].append(u)
#   return distance, predecessor


# def reconstruct_all_paths(predecessor, source, destination, path, payload):
#   path.append(destination)

#   if destination == source:
#     payload.append(path)
#     return payload

#   for u in predecessor[destination]:
#     if u not in path:  # dealing with cycles
#       new_path = path.copy()
#       reconstruct_all_paths(predecessor, source, u, new_path, payload)
#   return payload


# N, M = map(int, input().split())
# adj_list = {u: [] for u in range(1, N+1)}
# for _ in range(M):
#   A, B = map(int, input().split())
#   adj_list[A].append(B)
#   adj_list[B].append(A)

# distance, predecessor = dijkstra(adj_list, 1)
# all_paths = reconstruct_all_paths(predecessor, 1, N, [], [])
# print(len(all_paths))

N, M = map(int, input().split())
adj_list = {u: [] for u in range(1, N+1)}
for _ in range(M):
  A, B = map(int, input().split())
  adj_list[A].append(B)
  adj_list[B].append(A)

queue = [1]
dist = {u: None for u in range(N+1)}
path_count = {u: 0 for u in range(N+1)}
dist[1] = 0
path_count[1] = 1

for u in queue:
  for v in adj_list[u]:
    if dist[v] == None:
      dist[v] = dist[u]+1
      path_count[v] = path_count[u]
      queue.append(v)
    elif dist[v] == dist[u]+1:
      path_count[v] += path_count[u]

print(path_count[N] % (10**9+7))
