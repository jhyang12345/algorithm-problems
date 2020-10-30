# Given a list of words in a string, reverse the words in-place
# (ie don't create a new string and reverse the words).
# Since python strings are not mutable, you can assume the
# input will be a mutable sequence (like list).
#
# Here's an example and some starting code:

def reverse_words(w):
    s = ''.join(w)
    words = s.split()
    stack = []
    while w:
        w.pop()
    while words:
        word = words.pop()
        stack.append(word)
    for c in ' '.join(stack):
        w.append(c)

s = list("can you read this")
reverse_words(s)
print(''.join(s))
# this read you can
