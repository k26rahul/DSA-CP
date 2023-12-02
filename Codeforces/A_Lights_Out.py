grid = [list(map(int, input().split())) for _ in range(3)]
lights = [
    ['1' for _ in range(3)]
    for _ in range(3)
]


def new_state(curr_state, number):
    if curr_state == '1':
        return '1' if number % 2 == 0 else '0'
    return '0' if number % 2 == 0 else '1'


for i in range(3):
    for j in range(3):
        number = grid[i][j]
        lights[i][j] = new_state(lights[i][j], number)
        if i+1 < 3:
            lights[i+1][j] = new_state(lights[i+1][j], number)
        if i-1 >= 0:
            lights[i-1][j] = new_state(lights[i-1][j], number)
        if j+1 < 3:
            lights[i][j+1] = new_state(lights[i][j+1], number)
        if j-1 >= 0:
            lights[i][j-1] = new_state(lights[i][j-1], number)

print(*[''.join(row) for row in lights], sep='\n')
