def witnesses(heights):
    start = 0
    count = 0
    for h in heights[::-1]:
        if h > start:
            start = h
            count += 1
    return count

print(witnesses([3, 6, 3, 4, 1]))
