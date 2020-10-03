# Given two rectangles, find the area of intersection.
#
# Here's some starter code and a starter example:

class Rectangle():
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y

def intersection_area(rect1, rect2):
    top = min(rect1.max_y, rect2.max_y)
    bottom = max(rect1.min_y, rect2.min_y)
    left = max(rect1.min_x, rect2.min_x)
    right = min(rect1.max_x, rect2.max_x)
    if top < bottom or right < left:
        return 0
    return (top - bottom) * (right - left)


#  BBB
# AXXB
# AAA
rect1 = Rectangle(0, 0, 3, 2)
rect2 = Rectangle(1, 1, 3, 3)

print(intersection_area(rect1, rect2))
