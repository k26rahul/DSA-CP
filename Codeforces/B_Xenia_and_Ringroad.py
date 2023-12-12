n, m = map(int, input().split())
tasks = map(int, input().split())

time = 0
current_house = 1
for task in tasks:
  if task < current_house:
    time += n - current_house
    current_house = 0

  time += task - current_house
  current_house = task

print(time)
