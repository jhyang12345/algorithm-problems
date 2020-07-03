# Largest Product of 3 Elements
#

def maximum_product_of_three(arr):
    max_stack = []
    min_stack = []
    for x in arr:
        if len(max_stack) == 0 or x >= max_stack[0]:
            max_stack = [x] + max_stack
        elif len(max_stack) > 1 and (max_stack[0] >= x >= max_stack[1]):
            max_stack = max_stack[:1] + [x] + max_stack[1:]
        elif len(max_stack) > 0 and max_stack[-1] >= x:
            max_stack.append(x)

        if len(min_stack) == 0 or x <= min_stack[0]:
            min_stack = [x] + min_stack
        elif len(min_stack) > 1 and (min_stack[0] <= x <= min_stack[1]):
            min_stack = min_stack[:1] + [x] + min_stack[1:]
        elif len(min_stack) > 0 and min_stack[-1] <= x:
            min_stack.append(x)

        max_stack = max_stack[:3]
        min_stack = min_stack[:3]
    max_value = None
    a, b, c = max_stack
    x, y, z = min_stack
    max_value = a * b * c
    max_value = max(max_value, a * y * x)
    print(max_value)


arr = [-4, -4, 2, 8]
maximum_product_of_three(arr)
