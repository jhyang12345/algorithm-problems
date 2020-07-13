# A look-and-say sequence is defined as the integer sequence beginning with a single digit
# in which the next term is obtained by describing the previous term. An example is easier to understand:
#
# Each consecutive value describes the prior value.
#
# 1      #
# 11     # one 1's
# 21     # two 1's
# 1211   # one 2, and one 1.
# 111221 # #one 1, one 2, and two 1's.

def nth_sequence(n):
    cur = '1'
    i = 0
    while i < n:
        temp = ''
        s = cur[0]
        count = 1
        x = 1
        while x < len(cur):
            if s == cur[x]:
                count += 1
            else:
                temp += str(count) + s
                count = 1
                s = cur[x]
            x += 1
        temp += str(count) + s
        cur = temp
        i += 1
    return temp

for x in range(1, 21):
    print(nth_sequence(x))
