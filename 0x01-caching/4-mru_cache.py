#!/usr/bin/env python3
""" MRU Caching implementation """
from base_caching import BaseCaching  # Import BaseCaching

class MRUCache(BaseCaching):
    """ MRU Cache implementation """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        """ Add an item to the cache using MRU algorithm """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.used_keys.remove(key)  # Remove existing key to update MRU
        
        self.cache_data[key] = item
        self.used_keys.append(key)      # Add/re-add key to the end (MRU)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.used_keys.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        self.used_keys.remove(key)   # Remove the key from its current position
        self.used_keys.append(key)   # Add it to the end (most recently used)

        return self.cache_data[key]

