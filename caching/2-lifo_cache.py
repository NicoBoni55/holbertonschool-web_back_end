#!/usr/bin/python3
'''
Basic Dictionary: Create a class LIFOCache that inherits from BaseCaching
'''

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''
    Class LIFOCache
    '''
    def __init__(self):
        super().__init__()
        self.order_key = []

    def put(self, key, item):
        '''
        Add key/value pair to cache.
        '''
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order_key.remove(key)
            self.cache_data[key] = item
            self.order_key.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.order_key.pop(-2)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        '''
        Return value stored in `key` of cache.
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
