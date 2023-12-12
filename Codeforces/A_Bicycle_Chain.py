input()
pedal = list(map(int, input().split()))

input()
rear = list(map(int, input().split()))

max = 0
max_count = 0
for p in pedal:
  for r in rear:
    r_by_p = r/p

    if r_by_p == r//p:
      if r_by_p > max:
        max = r_by_p
        max_count = 0
      if r_by_p == max:
        max_count += 1

print(max_count)
