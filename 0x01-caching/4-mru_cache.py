#!/usr/bin/env python3
"""MRU Caching implementation."""

class BaseCaching:
    """
    Base class for caching systems.
    """
    MAX_ITEMS = 100
    cache_data = {}

    def __init__(self):
        """Initialize"""
        self.cache_data = {}

class MRUCache(BaseCaching):
    """
    MRU Cache implementation.
    """

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.used_keys = []

    def put(self, key, item):
        """
        Add an item to the cache using MRU algorithm.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.used_keys.remove(key)

        self.cache_data[key] = item
        self.used_keys.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = self.used_keys.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """
        Retrieve an item from the cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.used_keys.remove(key)
        self.used_keys.append(key)

        return self.cache_data[key]
