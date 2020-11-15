# Under the condition that a full binary tree is constructed in numerical Order
# given a number find the node in the quickest method

#  sample tree
#       1
#      /  \
#     2    3
#    / \  / \
#   4   5 6  7


def find_fastest_path(number):
    level = 0
    while number / (2 ** level) >= 1:
        level += 1
    level -= 1
    if number == 1:
        return []
    ret = []
    value = number - (2 ** level) + 1
    print(2 ** level)
    while level > 0:
        if value > (2 ** (level - 1)):
            value -= (2 ** (level - 1))
            ret.append('right')
        else:
            ret.append('left')
        level -= 1
    return ret



print(find_fastest_path(7))
print(find_fastest_path(6))
print(find_fastest_path(5))
print(find_fastest_path(4))

print(find_fastest_path(2))
print(find_fastest_path(3))
