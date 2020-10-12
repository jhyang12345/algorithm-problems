# Given a string, return the first recurring letter that appears.
# If there are no recurring letters, return None.
#
# Example:
# Input: qwertty
# Output: t
#
# Input: qwerty
# Output: None
# Here's some starter code:

def first_recurring_char(s):
    dict = {}
    for ch in s:
        if ch in dict:
            return ch
        else:
            dict[ch] = 'asdf'
    return None

print(first_recurring_char('qwertty'))
# t

print(first_recurring_char('qwerty'))
# None
