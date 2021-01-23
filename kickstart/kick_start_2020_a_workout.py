# Tambourine has prepared a fitness program so that she can become more fit! The program is made of N sessions.
# During the i-th session, Tambourine will exercise for Mi minutes.
# The number of minutes she exercises in each session are strictly increasing.
#
# The difficulty of her fitness program is equal to the maximum difference
# in the number of minutes between any two consecutive training sessions.
#
# To make her program less difficult, Tambourine has decided to add up to
# K additional training sessions to her fitness program. She can add these sessions anywhere
# in her fitness program, and exercise any positive integer number of minutes in each of them.
# After the additional training session are added, the number of minutes she exercises
# in each session must still be strictly increasing. What is the minimum difficulty possible?
#
# Input
# The first line of the input gives the number of test cases, T. T test cases follow.
# Each test case begins with a line containing the two integers N and K.
# The second line contains N integers, the i-th of these is Mi, the number
# of minutes she will exercise in the i-th session.
#

import sys
import heapq

def get_max_difficulty(nums, k):
    diff_q = []
    heapq.heapify(diff_q)
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        heapq.heappush(diff_q, -diff)
    for i in range(k):
        val = - heapq.heappop(diff_q)
        half = val // 2
        other_half = val - half
        heapq.heappush(diff_q, - half)
        heapq.heappush(diff_q, - other_half)

    return max(1, - heapq.heappop(diff_q))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    for i in range(1, n + 1):
        n, k = list(map(int, sys.stdin.readline().split()))
        nums = list(map(int, sys.stdin.readline().split()))
        print(f"Case #{i}: {get_max_difficulty(nums, k)}")
