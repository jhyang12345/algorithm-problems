# Given a list of meetings that will happen during a day, find the minimum number of meeting rooms that can fit all meetings.
#
# Each meeting will be represented by a tuple of (start_time, end_time), where both start_time
# and end_time will be represented by an integer to indicate the time. start_time will be inclusive,
# and end_time will be exclusive, meaning a meeting of (0, 10) and (10, 20) will only require 1 meeting room.
#
# Here's some examples and some starting code:

def meeting_rooms(meetings):
    # Fill this in.
    meetings.sort()
    queue = []
    ret = 0
    for x in meetings:
        start, end = x
        queue.append(x)
        while queue:
            if start >= queue[0][1]:
                queue.pop(0)
            else:
                break
        ret = max(ret, len(queue))
    return ret


# print 1
print(meeting_rooms([(0, 10), (10, 20)]))
# 1

print(meeting_rooms([(20, 30), (10, 21), (0, 50)]))
# 3 (all meetings overlap at time 20)
