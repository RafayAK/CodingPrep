"""
This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache.

It should be able to be initialized with a cache size n, and contain the following methods:

- set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item,
                   then it should also remove the least frequently used item.
                   If there is a tie, then the least recently used key should be removed.

- get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time
"""


# https://medium.com/@epicshane/a-python-implementation-of-lfu-least-frequently-used-cache-with-o-1-time-complexity-e16b34a3c49b
# http://dhruvbird.com/lfu.pdf


# doubly linked_list for Frequency_list
class FrequencyNode(object):
    def __init__(self, freq_value):
        self.nxt = self  # points to self because a doubly linked list
        self.prev = self  # points to self because a doubly linked list
        self.freq_value = freq_value  # represents set of cache nodes with same access frequency
        self.items = dict()  # dict of keys of LFUNodes with the same frequency, using it as a quick access list

    def remove_cache_item(self, key):
        del self.items[key]


class LFUNode(object):
    def __init__(self, data, parent):
        self.data = data
        self.parent = parent


class LFUCache(object):
    def __init__(self, capacity):
        self.cache = {}  # dictionary
        self.capacity = capacity
        self.frequency_list_head = FrequencyNode(0)

    @staticmethod
    def create_new_freq_node(value, prev, nxt):
        new_freq_node = FrequencyNode(value)
        new_freq_node.prev = prev
        new_freq_node.nxt = nxt
        prev.nxt = new_freq_node
        nxt.prev = new_freq_node
        return new_freq_node

    def delete_freq_node(self, freq_node):
        freq_node.prev.nxt = freq_node.nxt
        freq_node.nxt.prev = freq_node.prev

    def get(self, key):
        # get function is O(1) due to dictionary lookup
        if key not in self.cache:
            return -1

        temp = self.cache[key]  # hold the LFUNode

        freq_node = temp.parent
        next_freq_node = freq_node.nxt

        if next_freq_node is self.frequency_list_head or next_freq_node.freq_value != freq_node.freq_value+1:
            next_freq_node = self.create_new_freq_node(freq_node.freq_value+1, freq_node, next_freq_node)

        next_freq_node.items[key] = None
        temp.parent = next_freq_node

        freq_node.remove_cache_item(key)
        if len(freq_node.items) == 0:
            self.delete_freq_node(freq_node)

        return temp.data


    def get_lfu_item(self):
        if len(self.cache) == 0:
            print("Cache Empty!")
            return -1
        else:
            # type casting dict to list gives keys in a list
            key = list(self.frequency_list_head.nxt.items)[0]
            lfu_cache_node = self.cache[list(self.frequency_list_head.nxt.items)[0]]

            print("key: {}, value: {} ----- belongs to frequency node #{}".format(list(self.frequency_list_head.nxt.items)[0],
                                          lfu_cache_node.data, lfu_cache_node.parent.freq_value),
                  )

            return key, lfu_cache_node.parent

    def update_data(self, key, value):
        self.get(key)  # get the data, mainly used here to update the cache LFUNode's postions
        self.cache[key].data = value  # updates the data of the LFUNode

    def set(self, key, value):
        if key in self.cache:
            # found element update the data value and move the LFUNode
            # to the next frequency node
            self.update_data(key, value)
        else:
            # check if about to overflow
            if len(self.cache) == self.capacity:
                # delete least frequently used cache element
                k, par = self.get_lfu_item()
                del self.cache[k]
                del par.items[k]
            freq_node = self.frequency_list_head.nxt

            if freq_node.freq_value is not 1:
                freq_node = self.create_new_freq_node(value=1, prev=self.frequency_list_head, nxt=freq_node)

            # freq_node.items.add(key)
            freq_node.items[key] = None
            self.cache[key] = LFUNode(value, freq_node)






if __name__ == '__main__':
    lfu = LFUCache(6)
    lfu.set('a', 1)
    lfu.set('b', 1)
    lfu.set('c', 1)
    lfu.set('x', 1)
    lfu.set('y', 1)
    lfu.set('z', 1)

    # this should give least recently used item 'a' as frequency is same for all right now
    lfu.get_lfu_item()

    for i in range(2, 10):
        lfu.set('c', i)

    lfu.get_lfu_item() # a is still lfu

    for i in range(2, 6):
        lfu.set('b', i)

    lfu.get_lfu_item() # a is still lfu

    lfu.set('z', 2)
    lfu.set('a', 2)

    lfu.get_lfu_item() # x is the lfu

    lfu.set('p', 1)  # x will be kicked out

    lfu.get_lfu_item()  # y is the lfu now

    lfu.set('p', 2)
    lfu.set('y', 2)
    lfu.get_lfu_item()  # z is the lfu

    lfu.set('p', 1)
    lfu.get_lfu_item()  # a should be the answer

    lfu.get('q') # z will be kicked out
    lfu.get_lfu_item() # y should be the answer

