import sys
# https://www.acmicpc.net/problem/13460

n, m = map(int, sys.stdin.readline().split())

drawing = []
for _ in range(n):
    drawing.append(list(sys.stdin.readline().strip()))

rx, ry = 0, 0
bx, by = 0, 0
ox, oy = 0, 0

for y in range(m):
    for x in range(n):
        if drawing[x][y] == "R":
            rx, ry = x, y
            drawing[x][y] = "."
        if drawing[x][y] == "B":
            bx, by = x, y
            drawing[x][y] = "."
        if drawing[x][y] == "O":
            ox, oy = x, y
            drawing[x][y] = "."

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

queue = [[rx, ry, bx, by, -1, 0]]

def red_first(rx, ry, bx, by, direction):
    dx, dy = direction
    if dx > 0:
        return rx > bx
    elif dx < 0:
        return rx < bx
    elif dy > 0:
        return ry > by
    elif dy < 0:
        return ry < by
    return True

def will_be_in_hole_or_blocked(x, y, direction):
    dx, dy = direction
    return drawing[x + dx][y + dy] != '#' and not ((x == ox) and (y == oy))
def in_hole(x, y):

    return x == ox and y == oy

def balls_to_end(rx, ry, bx, by, direction):
    dx, dy = direction
    if red_first(rx, ry, bx, by, direction):
        # print("RED")
        while will_be_in_hole_or_blocked(rx, ry, direction):
            rx += dx
            ry += dy
        while will_be_in_hole_or_blocked(bx, by, direction) and not (bx == rx and by == ry):
            bx += dx
            by += dy
        if (bx == rx and by == ry) and not in_hole(bx, by):
            bx -= dx
            by -= dy
    else:
        # print("BLUE")
        while will_be_in_hole_or_blocked(bx, by, direction):
            bx += dx
            by += dy
        while will_be_in_hole_or_blocked(rx, ry, direction) and not (bx == rx and by == ry):
            rx += dx
            ry += dy
        if (bx == rx and by == ry) and not in_hole(rx, ry):
            rx -= dx
            ry -= dy
    return [rx, ry, bx, by]
    


index = 0
while index < len(queue):
    # last_dir is the index of direction
    rx, ry, bx, by, last_dir, count = queue[index]
    if count > 10:
        print(-1)
        break
    if bx == ox and by == oy:
        index += 1
        continue
    elif rx == ox and ry == oy:
        print(count)
        break
    for i, direction in enumerate(directions):
        if last_dir == -1 or last_dir != i:
            buffer = balls_to_end(rx, ry, bx, by, direction)
            queue.append(buffer + [i, count + 1])
    index += 1