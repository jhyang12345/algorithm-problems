# Given a list of points, an interger k, and a point p, find the k closest points to p.
#
# Here's an example and some starter code:

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def closest_points(points, k, p):
    for point in points:
        point.x = point.x - p.x
        point.y = point.y - p.y

    points.sort(key=lambda x: x.x ** 2 + x.y ** 2)
    for point in points:
        point.x = point.x + p.x
        point.y = point.y + p.y
    return points[:k]

points = [
    Point(0, 0),
    Point(1, 1),
    Point(2, 2),
    Point(3, 3),
]
print(closest_points(points, 2, Point(0, 2)))
# [(0, 0), (1, 1)]
