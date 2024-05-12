year = int(input())

while True:
  year += 1
  if len(list(str(year))) == len(set(str(year))):
    print(year)
    break
