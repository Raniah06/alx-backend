#!/usr/bin/python3
"""
Module for implementing an MRU (Most Recently Used) Cache.

This module contains the MRUCache class that inherits from the BaseCaching
class and implements the MRU caching algorithm. The cache stores items up to
a maximum limit, discarding the most recently used item when the limit is exceeded.
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class that implements a Most Recently Used (MRU) cache.

    This class inherits from BaseCaching and implements the put and get methods.
    The cache stores key-value pairs and evicts the most recently used item
    when the cache exceeds the maximum allowed items.
    """

    def __init__(self):
        """
        Initialize the MRUCache class.
        
        This constructor calls the parent class (BaseCaching) to initialize
        the cache data and initializes a list to track access order.
        """
        super().__init__()
        self.access_order = []  # Tracks the order in which keys are accessed

    def put(self, key, item):
        """
        Add an item to the cache or update an existing item.
        
        If the cache exceeds the maximum allowed items, the most recently used
        item is discarded.

        Args:
            key (str): The key to store the item.
            item (str): The value associated with the key.

        If either key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # If key exists, update item and reorder access list
            self.access_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Evict the most recently used item
            mru_key = self.access_order.pop()  # Most recently used key
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add or update the cache
        self.cache_data[key] = item
        self.access_order.append(key)  # Mark this key as most recently used

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key to look for in the cache.

        Returns:
            str: The value associated with the key, or None if the key is not found.

        If the key exists, it is marked as most recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        # Mark the key as most recently used
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
