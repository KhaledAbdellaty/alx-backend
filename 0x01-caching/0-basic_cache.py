#!/usr/bin/env python3
from base_caching import BaseCaching
"""BasicCache class"""


class BasicCache(BaseCaching):
    """A class that inherits from
    BaseCaching and is a caching system"""

    def put(self, key, item):
        """A function that put the item value
        for the key in cach data dict"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """A function that get the item value for
        the key in cach data"""
        if key is None or\
                self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
