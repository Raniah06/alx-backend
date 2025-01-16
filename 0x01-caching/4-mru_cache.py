#!/usr/bin/python3
""" MRU Caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache defines an MRU caching system. """

    def __init__(self):
        """ Initialize the class with the parent's init method. """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache using MRU algorithm.
        If `key` or `item` is None, do nothing.
        """
        if key is not None and item is not None:
            # If the cache exceeds the max number of items, discard the MRU item.
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the most recently used item (the last item in the dictionary)
                discarded_key, discarded_value = self.cache_data.popitem()
                print("DISCARD:", discarded_key)

            # Add or update the cache with the new item.
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item by key from the cache.
        If `key` is None or does not exist, return None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
