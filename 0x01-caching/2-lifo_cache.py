#!/usr/bin/env python3
"""LIFOCache class is a caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """A class that inherits from
    BaseCaching and is a caching system"""

    def __init__(self):
        """An init method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """A function that put the item value
        for the key in cach data dict
        put in cache (LIFO algorithm)"""
        if key is None or item is None:
            return
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            last_key, _ = self.cache_data.popitem(True)
            print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """A function that get the item value for
        the key in cach data"""
        if key is None or\
                self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
