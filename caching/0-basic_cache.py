#!/usr/bin/python3
'''
Basic Dictionary: Create a class BasicCache that inherits from BaseCaching
'''

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''
    A basic cache.
    put - method that adds a key/value pair to cache
    get - method that retrieves a key/value pair from cache
    '''

    def put(self, key, item):
        '''
        Add key/value pair to cache.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''
        Return value stored in `key` of cache.
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
