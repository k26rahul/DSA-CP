T = int(input())

for _ in range(T):
  n = T = int(input())
  string = input()
  last_3 = ''
  last_6 = ''
  map_count = 0
  pie_count = 0
  map_pie_count = 0
  for letter in string:
    if len(last_3) == 3:
      last_3 = last_3[1:]
    if len(last_6) == 6:
      last_6 = last_6[1:]

    last_3 += letter
    last_6 += letter

    if last_3 == 'map':
      map_count += 1
    if last_3 == 'pie':
      pie_count += 1
    if last_6 == 'mappie':
      map_pie_count += 1

    # print(last_3)

  print(map_count + pie_count - map_pie_count)
  # print(map_count, pie_count, map_pie_count)
