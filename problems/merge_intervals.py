# Merge Overlapping Intervals

def merge(overlaps):
    overlaps.sort()
    pairs = []
    for pair in overlaps:
        if len(pairs) == 0:
            pairs.append(pair)
        else:
            last = pairs[-1]
            if pair[0] <= last[1]:
                pairs[-1] = (last[0], max(last[1], pair[1]))
            else:
                pairs.append(pair)
    print(pairs)





overlaps = [(1, 3), (5, 8), (4, 10), (20, 25)]

merge(overlaps)
