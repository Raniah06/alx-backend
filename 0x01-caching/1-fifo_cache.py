#!/usr/bin/python3
""" FIFO Caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system. """

    def __init__(self):
        """ Initialize the class with the parent's init method. """
        super().__init__()
        self.queue = []  # To keep track of the insertion order.

    def put(self, key, item):
        """
        Add an item to the cache using FIFO algorithm.
        If `key` or `item` is None, do nothing.
        """
        if key is not None and item is not None:
            # If the key is new and the cache is full, remove the oldest item.
            if key not in self.cache_data and len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                oldest_key = self.queue.pop(0)  # FIFO: Remove the first inserted key.
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

            # Add or update the cache and the queue.
            if key not in self.queue:
                self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item by key from the cache.
        If `key` is None or does not exist, return None.
        """
        return self.cache_data.get(key)
