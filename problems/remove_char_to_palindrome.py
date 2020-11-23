# Given a string, determine if you can remove any character to create a palindrome.
#
# Here's some examples and some starter code:
# https://leetcode.com/problems/valid-palindrome-ii/submissions/

def create_palindrome(s):
    start = 0
    end = len(s) - 1
    skip_indexes = []
    emptied = False
    while start < end:
        x = s[start]
        y = s[end]
        print(s, skip_indexes, x, y)
        if x != y:
            if not skip_indexes and not emptied:
                skip_indexes += [start, end]
                continue
            elif skip_indexes:
                back = skip_indexes.pop()
                if skip_indexes:
                    end = back - 1
                    start = skip_indexes[0]
                else:
                    start = back + 1
                    end = len(s) - back - 1
                print(skip_indexes, start, end)
                if not skip_indexes:
                    emptied = True
                continue
            if emptied:
                return False
        start += 1
        end -= 1
    if not emptied and not skip_indexes:
        return False
    return True



print(create_palindrome("abcdcbea"))
# True
print(create_palindrome("abccba"))
# False
print(create_palindrome("abccaa"))
# False
