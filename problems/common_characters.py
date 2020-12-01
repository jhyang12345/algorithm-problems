# Given a list of strings, find the list of characters that appear in all strings.
#
# Here's an example and some starter code:

def common_characters(strs):
    ret = None
    for word in strs:
        a = set()
        for ch in word:
            a.add(ch)
        if ret == None:
            ret = a
        ret = ret & a
    return list(ret)

print(common_characters(['google', 'facebook', 'youtube']))
# ['e', 'o']
