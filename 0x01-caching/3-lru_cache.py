#!/usr/bin/python3
""" LRU Caching """

from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):
    """ LRUCache defines a LRU caching system. """

    def __init__(self):
        """ Initialize the class with the parent's init method. """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item to the cache using LRU algorithm.
        If `key` or `item` is None, do nothing.
        """
        if key is not None and item is not None:
            # If the cache exceeds the max number of items, discard the LRU item.
            if (len(self.cache_data) >= 
                BaseCaching.MAX_ITEMS:
                discarded_key, discarded_value = self.cache_data.popitem(last=False))
                print("DISCARD:", discarded_key)

            # Add or update the cache with the new item and mark it.
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)  # Mark as recently used

    def get(self, key):
        """
        Retrieve an item by key from the cache.
        If `key` is None or does not exist, return None.
        """
        if key is not None and key in self.cache_data:
            # Move the accessed item to the end to mark it as recently used.
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
