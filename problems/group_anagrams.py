import collections

# Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same letters).

def groupAnagramWords(strs):
    groups = {}
    for word in strs:
        repr = str(sorted(list(word)))
        if repr in groups:
            groups[repr].append(word)
        else:
            groups[repr] = [word]
    return list(groups.values())

print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]
