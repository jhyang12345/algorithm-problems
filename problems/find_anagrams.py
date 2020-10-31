# Given 2 strings s and t, find and return all indexes in string s where t is an anagram.
#
# Here's an example and some starter code:

def find_anagrams(s, t):
    ret = []
    n = len(s)
    m = len(t)
    start = 0
    end = 0
    char_dict = {}
    t_dict = {}
    for c in t:
        if c not in t_dict:
            t_dict[c] = 1
            char_dict[c] = 0
        else:
            t_dict[c] += 1
    while start <= n - m:
        if end - start < m:
            ch = s[end]
            if ch not in char_dict:
                char_dict[ch] = 1
            else:
                char_dict[ch] += 1
            end += 1
        else:
            ch = s[start]
            char_dict[ch] -= 1
            start += 1
        if end - start == m:
            equal = True
            for ch in t_dict:
                if t_dict[ch] != char_dict[ch]:
                    equal = False
                    break
            if equal:
                ret.append(start)
    return ret

print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]
