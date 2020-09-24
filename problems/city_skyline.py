# Given a list of building in the form of (left, right, height),
# return what the skyline should look like.
# The skyline should be in the form of a list of (x-axis, height),
# where x-axis is the next point where there is a change in height starting from 0,
# and height is the new height starting from the x-axis.
#
# Here's some starter code:

def generate_skyline(buildings):
    height = 0
    width = 0
    for b in buildings:
        left, right, h = b
        height = max(height, h)
        width = max(width, right)
    grid = [[' ' for _ in range(width)] for __ in range(height)]
    for y in range(1, len(grid) + 1):
        for x in range(1, len(grid[0]) + 1):
            for i, g in enumerate(buildings):
                left, right, height = g
                if left <= x <= right and y < height:
                    grid[y - 1][x - 1] = str(i + 1)
    ret = ""

    for g in grid[::-1]:
        ret += ''.join(g)
        ret += "\n"
    return ret


#            2 2 2
#            2 2 2
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
# pos: 1 2 3 4 5 6 7 8 9
print(generate_skyline([(2, 8, 3), (4, 6, 5)]))
# [(2, 3), (4, 5), (7, 3), (9, 0)]
