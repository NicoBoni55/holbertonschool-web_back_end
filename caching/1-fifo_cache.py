#!/usr/bin/python3
'''
Basic Dictionary: Create a class FIFOCache that inherits from BaseCaching
'''

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    Class FIFOCache
    '''

    def put(self, key, item):
        '''
        Add key/value pair to cache.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = list(self.cache_data)[0]
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        '''
        Return value stored in `key` of cache.
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
