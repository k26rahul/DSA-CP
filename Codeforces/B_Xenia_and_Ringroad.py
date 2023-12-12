n, m = map(int, input().split())
tasks = map(int, input().split())

time = 0
current_house = 0
for task in tasks:
  if task < current_house:
    time += n - current_house
    current_house = 0
  if task > current_house:
    current_house = task
  time += task

print(time)
