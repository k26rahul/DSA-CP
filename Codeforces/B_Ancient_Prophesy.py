prophesy = input()
n = len(prophesy)
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

dates = []
# dates = {}

day = ''
month = ''
year = ''

waiting_for_dash = False
i = -1
while i < n-1:
  i += 1

  if prophesy[i] == '-':
    if waiting_for_dash:
      waiting_for_dash = False
    else:
      day = ''
      month = ''
      year = ''
    continue

  if waiting_for_dash:
    waiting_for_dash = False
    i -= 2
    day = ''
    month = ''
    year = ''

print(dates)

# max_date = ''
# max_count = 0
# for date, count in dates.items():
#   if int(count) > max_count:
#     max_date = date
#     max_count = int(count)

# print(f'{max_date[:2]}-{max_date[2:4]}-{max_date[-4:]}')
