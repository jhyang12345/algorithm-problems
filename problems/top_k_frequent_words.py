# Given a non-empty list of words, return the k most frequent words. The output should be sorted from highest to lowest frequency, and if two words have the same frequency, the word with lower alphabetical order comes first. Input will contain only lower-case letters.
#
# Example:
# Input: ["daily", "interview", "pro", "pro",
# "for", "daily", "pro", "problems"], k = 2
# Output: ["pro", "daily"]
class Solution(object):
    def topKFrequent(self, words, k):
        counter = {}
        for word in words:
            if word not in counter:
                counter[word] = 1
            else:
                counter[word] += 1
        word_list = sorted(list(counter.keys()), key=lambda x: -counter[x])
        return word_list[:k]

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(Solution().topKFrequent(words, k))
# ['pro', 'daily']
