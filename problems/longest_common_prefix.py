# Given a list of strings, find the longest common prefix between all strings.
#
# Here's some examples and some starter code.

class Node:
    def __init__(self, ch, is_terminal=False):
        self.ch = ch
        self.is_terminal = is_terminal
        self.children = {}

    def __repr__(self):
        return str(self.children)

def longest_common_prefix(strs):
    root = Node('')
    for word in strs:
        next = root
        for i, ch in enumerate(word):
            next_node = None
            if ch not in next.children:
                next_node = Node(ch)
            else:
                next_node = next.children[ch]
            if i == (len(word) - 1):
                next_node.is_terminal = True
            next.children[ch] = next_node
            next = next_node
    next = root
    ret = ''
    while next:
        if next.is_terminal:
            ret += next.ch
            break
        elif len(next.children.keys()) > 1 or len(next.children.keys()) == 0:
            ret += next.ch
            break
        elif len(next.children.keys()) == 1:
            ret += next.ch
            next = list(next.children.values())[0]
        else:
            break
    return ret


print(longest_common_prefix(['helloworld', 'hellokitty', 'hell']))
# hell

print(longest_common_prefix(['daily', 'interview', 'pro']))
# ''


print(longest_common_prefix(['something', 'someof']))
# ''
