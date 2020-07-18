def longest_substring_k_distinct(text, threshold):
    dict = {}
    max_len = 0
    start = 0
    chars = []
    for i, c in enumerate(text):
        dict[c] = i
        if c not in chars:
            chars.append(c)

            if len(chars) > threshold:
                min_end = len(text)
                selected = ''
                for ch in chars:
                    min_end = min(dict[ch], min_end)
                    if min_end == dict[ch]:
                        selected = ch
                start = min_end + 1
                chars.pop(chars.index(selected))
        # print(chars)
        # print(start, i)
        max_len = max(max_len, 1 + i - start)
    return max_len


print(longest_substring_k_distinct('aabcdefff', 3))
