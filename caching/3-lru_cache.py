#!/usr/bin/python3
'''
Basic Dictionary: Create a class LRUCache that inherits from BaseCaching
'''

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''
    Class LRUCache
    '''
    def __init__(self):
        super().__init__()
        self.order_data = []

    def put(self, key, item):
        '''
        Add key/value pair to cache.
        '''
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order_data.remove(key)
            self.cache_data[key] = item
            self.order_data.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.order_data.pop(0)
            self.cache_data.pop(last_key)
            print(f"DISCARD: {last_key}")

    def get(self, key):
        '''
        Return value stored in `key` of cache.
        '''
        if key is not None and key in self.cache_data:
            self.order_data.remove(key)
            self.order_data.append(key)
            return self.cache_data[key]
        return None
