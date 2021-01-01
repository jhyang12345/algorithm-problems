# Find all words that are concatenations of a list.
#
# Input:
# ["tech", "lead", "techlead", "cat", "cats", "dog", "catsdog"]
#
# Output:
# ['techlead', 'catsdog']
# https://leetcode.com/problems/concatenated-words/submissions/

class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        words.sort(key=lambda x: len(x))
        ret = []
        for word in words:
            starts = [0]
            if not word:
                continue
            while starts:
                start = starts.pop()
                if start == len(word):
                    ret.append(word)
                    break
                buffer = word[start:]
                for w in words:
                    if word == w:
                        continue
                    elif len(w) > len(buffer):
                        break
                    elif buffer.startswith(w):
                        if (start + len(w)) == len(word):
                            ret.append(word)
                            starts = []
                            break
                        if len(w) > 0:
                            starts.append(start + len(w))
        return ret

input = []

print(Solution().findAllConcatenatedWordsInADict(input))
