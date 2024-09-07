"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement an LRU (Least Recently Used) cache.
It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in
                 the cache and we are adding a new item,
                 then it should also remove the least recently used item.

get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
"""

class lru:
    def __init__(self, n):
        self._cache = dict()
        self._cache_size = n

    def set(self, key, value):
        if len(self._cache) == 0 or len(self._cache) < self._cache_size:
            # add value t dict
            self._cache[key] = value

        else:
            del(self._cache[list(self._cache.keys())[0]])

            # now add new data
            self._cache[key] = value

            assert len(self._cache) == self._cache_size

    def get(self, key):
        if key in self._cache:
            return self._cache[key]
        else:
            return None


if __name__ == '__main__':
    lru_cache = lru(5)

    assert not lru_cache.get(key='a')

    lru_cache.set('a', 1)
    assert lru_cache.get(key='a') == 1
    lru_cache.set('b', 2)
    lru_cache.set('c', 3)
    lru_cache.set('d', 4)
    lru_cache.set('f', 6)
    lru_cache.set('e', 5)
    assert not lru_cache.get(key='a')
    assert lru_cache.get('e') == 5




