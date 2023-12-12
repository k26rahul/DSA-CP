n = int(input())

team_a = ''
team_b = ''

goals_a = 0
goals_b = 0

for _ in range(n):
  team = input()
  if not team_a:
    team_a = team

  if team == team_a:
    goals_a += 1
  else:
    team_b = team
    goals_b += 1

print(team_a if goals_a > goals_b else team_b)
