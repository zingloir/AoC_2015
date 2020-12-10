with open('input') as f:
    lines = f.readlines()


# Alles auf on setzen
def turn_on(row, start, end):
    l = start
    while l <= end:
        grid[row][l] = grid[row][l] + 1
        l += 1


# Alles auf off setzen
def turn_off(row, start, end):
    l = start
    while l <= end:
        if grid[row][l] <= 1:
            grid[row][l] = 0
        else:
            grid[row][l] = grid[row][l] - 1
        l += 1

# Zustand switchen
def toggle(row, start, end):
    l = start
    while l <= end:
        grid[row][l] = grid[row][l] + 2
        l += 1


# Input bereinigen
def clean_input():
    i = 0
    while i < len(lines):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = lines[i].split(' ')
        if lines[i][0] == 'turn':
            del lines[i][0]
        del lines[i][2]
        i += 1


# Programm
grid = [0] * 1000
i = 0
while i < len(grid):
    grid[i] = [0] * 1000
    i += 1
clean_input()

for line in lines:
    startx = int(line[1][:line[1].find(',')])
    starty = int(line[1][line[1].find(',') + 1:])
    endx = int(line[2][:line[2].find(',')])
    endy = int(line[2][line[2].find(',') + 1:])

    if line[0] == 'on':
        i = starty
        while i <= endy:
            turn_on(i, startx, endx)
            i += 1

    elif line[0] == 'off':
        i = starty
        while i <= endy:
            turn_off(i, startx, endx)
            i += 1

    elif line[0] == 'toggle':
        i = starty
        while i <= endy:
            toggle(i, startx, endx)
            i += 1

sum = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        sum += grid[i][j]
print(sum)
