# Given a list of points as a tuple (x, y) and an integer k, find the k closest points to the origin (0, 0).
#
# Here's an example and some starter code:

def closest_points(points, k):
    p = sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)
    return p[:k]

print(closest_points([(0, 0), (1, 2), (-3, 4), (3, 1)], 2))
# [(1, 2), (0, 0)]
