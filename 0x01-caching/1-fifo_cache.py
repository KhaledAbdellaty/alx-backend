#!/usr/bin/env python3
"""FIFOCache class is a caching system"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """A class that inherits from
    BaseCaching and is a caching system"""

    def __init__(self):
        """An init method"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """A function that put the item value
        for the key in cach data dict.
        put in cache (FIFO algorithm)"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            discard_item, _ = self.cache_data.popitem(False)
            print(f"DISCARD: {discard_item}")

    def get(self, key):
        """A function that get the item value for
        the key in cach data"""
        if key is None or\
                self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
