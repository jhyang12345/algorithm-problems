import heapq

# Very important question !!!!!!!!!!
# https://letstalkalgorithms.com/meeting-rooms-leetcode/

# Look into this question as well for reference
# https://leetcode.com/problems/car-pooling/
def room_scheduling(schedules):
    schedules.sort()
    queue = []
    heapq.heapify(queue)
    count = 0
    ret = 0
    for schedule in schedules:
        start, end = schedule
        if not queue:
            heapq.heappush(queue, end)
            count += 1
        elif start < heapq.nsmallest(1, queue)[0]:
            heapq.heappush(queue, end)
            count += 1
        else:
            heapq.heappop(queue)
            count -= 1
        ret = max(ret, count)
    print(schedules)
    return ret

schedules = [(30, 75), (0, 50), (60, 150)]
print(room_scheduling(schedules))


schedules = [(30, 75), (30, 50), (60, 150)]
print(room_scheduling(schedules))

schedules = [[0, 30],[5, 10],[15, 20]]
print(room_scheduling(schedules))
