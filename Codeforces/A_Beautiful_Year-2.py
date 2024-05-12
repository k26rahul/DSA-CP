year = int(input())
beautiful_year = year

found = False
while not found:
    beautiful_year += 1
    if len(set(str(beautiful_year))) == 4:
        found = True

print(beautiful_year)
