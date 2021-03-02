# Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping
# intervals that cover all the intervals in the input.

def merge(intervals):
    intervals.sort()
    if not intervals:
        return []
    cur = intervals[0]
    ret = []
    for inter in intervals[1:]:
        a, b = cur
        x, y = inter
        if x > b:
            ret.append(cur)
            cur = inter
        else:
            cur = [a, max(b, y)]
    ret.append(cur)
    return ret

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))

# https://leetcode.com/problems/merge-intervals/submissions/
