# Given a list of words, for each word find the shortest unique prefix.
# You can assume a word will not be a substring of another word
# (ie play and playing won't be in the same words list)

# Example
# Input: ['joma', 'john', 'jack', 'techlead']
# Output: ['jom', 'joh', 'ja', 't']
# Here's some starter code:

# class Node:
#     def __init__(self, letter, is_end=False):

def shortest_unique_prefix(words):
    dict = {}
    for word in words:
        cur = dict
        for letter in word:
            if letter not in cur:
                cur[letter] = {'asdf': 1}
            else:
                cur[letter]['asdf'] += 1
            cur = cur[letter]
    prefixes = []
    for word in words:
        cur = dict
        ret = ""
        for letter in word:
            ret += letter
            if cur[letter]['asdf'] == 1:
                break
            cur = cur[letter]
        prefixes.append(ret)
    return prefixes

print(shortest_unique_prefix(['joma', 'john', 'jack', 'techlead']))
# ['jom', 'joh', 'ja', 't']
