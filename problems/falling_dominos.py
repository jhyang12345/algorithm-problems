# https://leetcode.com/problems/push-dominoes/

def solve_dominos(board):
    right_value = [0 for _ in len(board)]
    left_value = [0 for _ in len(board)]
    for i, x in enumerate(board):
        if x == 'R':
            right_value[i] = 1
        elif x == '.':
            if i > 0 and right_value[i - 1] > 0:
                right_value[i] = right_value[i - 1] + 1
    print(right_value)
    for i, x in enumerate(board):
        if x == 'R':
            right_value[i] = 1
        elif x == '.':
            if i > 0 and right_value[i - 1] > 0:
                right_value[i] = right_value[i - 1] + 1

print(solve_dominos('..R...L..R.'))
