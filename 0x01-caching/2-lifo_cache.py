#!/usr/bin/python3
""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system. """

    def __init__(self):
        """ Initialize the class with the parent's init method. """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using LIFO algorithm.
        If `key` or `item` is None, do nothing.
        """
        if key is not None and item is not None:
            # If the cache exceeds the max number of items, discard the last item inserted.
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]  # Get the last inserted key.
                del self.cache_data[last_key]
                print("DISCARD:", last_key)

            # Add or update the cache.
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item by key from the cache.
        If `key` is None or does not exist, return None.
        """
        return self.cache_data.get(key)
