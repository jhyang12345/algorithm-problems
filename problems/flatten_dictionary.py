# Given a nested dictionary, flatten the dictionary,
# where nested dictionary keys can be represented through dot notation.
#
# Example:
# Input: {
#   'a': 1,
#   'b': {
#     'c': 2,
#     'd': {
#       'e': 3
#     }
#   }
# }
# Output: {
#   'a': 1,
#   'b.c': 2,
#   'b.d.e': 3
# }
# You can assume there will be no arrays, and all keys will be strings.
#
# Here's some starter code:

def flatten_dictionary(d):
    queue = [(d, None)]
    ret = []
    while queue:
        cur, key = queue.pop(0)
        if isinstance(cur, dict):
            for k in cur:
                if key:
                    queue.append((cur[k], f'{key}.{k}'))
                else:
                    queue.append((cur[k], f'{k}'))
        else:
            ret.append((key, cur))
    d = {key: cur for key, cur in ret}
    return d

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
