# Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

def find_ranges(nums):
    last = None
    start = None
    ret = []
    for x in nums:
        if last == None:
            start = x
        elif x != last + 1:
            ret.append(f"{start}->{last}")
            start = x
        last = x
    ret.append(f"{start}->{last}")
    return ret
print(find_ranges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']
