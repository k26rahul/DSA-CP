prophesy = input()
n = len(prophesy)
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# dates = []
dates = {}

day = ''
month = ''
year = ''

expect_a_dash = False
i = -1
while i < n-1:
  i += 1
  # print(prophesy[i], day, month, year, expect_a_dash)

  if prophesy[i] == '-':
    expect_a_dash = False
    if prophesy[i+1] == '-':
      day = ''
      month = ''
      year = ''
    continue

  if expect_a_dash:
    expect_a_dash = False
    day = ''
    month = ''
    year = ''

  if len(day) != 2:
    day += prophesy[i]
    if len(day) == 2:
      expect_a_dash = True
    continue

  if len(month) != 2:
    month += prophesy[i]
    if len(month) == 2:
      expect_a_dash = True
    continue

  if len(year) != 4:
    year += prophesy[i]
    if len(year) == 4:
      if 2013 <= int(year) <= 2015:
        if 1 <= int(month) <= 12:
          if 1 <= int(day) <= days_in_month[int(month)]:
            # dates.append((day, month, year))
            date = day + month + year
            if date in dates:
              dates[date] += 1
            else:
              dates[date] = 1

      day = ''
      month = ''
      year = ''

      i -= 2

# print(dates)

max_date = ''
max_count = 0
for date, count in dates.items():
  if int(count) > max_count:
    max_date = date
    max_count = int(count)

print(f'{max_date[:2]}-{max_date[2:4]}-{max_date[-4:]}')
