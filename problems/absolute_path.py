# Given a file path with folder names, '..' (Parent directory), and '.' (Current directory),
# return the shortest possible file path (Eliminate all the '..' and '.').
#
# Example
# Input: '/Users/Joma/Documents/../Desktop/./../'
# Output: '/Users/Joma/'
def shortest_path(file_path):
    parts = file_path.split("/")
    stack = []
    for part in parts:
        if part == '..':
            stack.pop()
        elif part == '.':
            continue
        else:
            stack.append(part)
    return '/'.join(stack)


print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))
