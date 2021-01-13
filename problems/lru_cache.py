# LRU cache is a cache data structure that has limited space, and once there are more items
# in the cache than available space, it will preempt the least recently used item.
# What counts as recently used is any item a key has 'get' or 'put' called on it.
#
# Implement an LRU cache class with the 2 functions 'put' and 'get'. 'put' should place
# a value mapped to a certain key, and preempt items if needed. 'get' should return the
# value for a given key if it exists in the cache, and return None if it doesn't exist.
#
# Here's some examples and some starter code.

class LRUCache:
    def __init__(self, space):
        # Fill this in.
        self.stack = []
        self.dict = {}
        self.space = space


    def get(self, key):
        if key not in self.dict:
            return None
        return self.dict[key]

    def put(self, key, value):
        if key in self.dict:
            pass
        else:
            if len(self.stack) == self.space:
                remove_key = self.stack.pop()
                del self.dict[remove_key]
            self.stack.append(key)
        self.dict[key] = value

cache = LRUCache(2)

cache.put(3, 3)
cache.put(4, 4)
print(cache.get(3))
# 3
print(cache.get(2))
# None

cache.put(2, 2)

print(cache.get(4))
# None (pre-empted by 2)
print(cache.get(3))
# 3
