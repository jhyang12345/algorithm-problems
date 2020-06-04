# Given a string, find the length of the longest substring without repeating characters.
#
# Here is an example solution in Python language. (Any language is OK to use in an interview, though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)
#
# class Solution:
#   def lengthOfLongestSubstring(self, s):
#     # Fill this in.
#
# print Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx')

import sys

def longest_no_repeat_string(text):
    dict = {}
    last = 0
    max_len = 0
    for i, x in enumerate(text):
        if x in dict:
            last = max(dict[x] + 1, last)
        dict[x] = i
        max_len = max(max_len, i - last + 1)

    return max_len



if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(text)
    ret = longest_no_repeat_string(text)
    print(ret)
