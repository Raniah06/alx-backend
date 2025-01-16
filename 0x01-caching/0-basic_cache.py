#!/usr/bin/python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines a basic caching system without any limit. """

    def put(self, key, item):
        """
        Add an item to the cache.
        If either `key` or `item` is None, do nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item by key from the cache.
        If `key` is None or does not exist, return None.
        """
        return self.cache_data.get(key)
