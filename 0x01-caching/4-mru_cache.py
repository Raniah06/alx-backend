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
    The cache stores key-value pairs and evicts the least recently used item
    when the cache exceeds the maximum allowed items.
    """
    
    def __init__(self):
        """
        Initialize the MRUCache class.
        
        This constructor calls the parent class (BaseCaching) to initialize
        the cache data and other required properties.
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item to the cache or update an existing item.
        
        If the cache exceeds the maximum allowed items, the least recently used
        item is discarded.

        Args:
            key (str): The key to store the item.
            item (str): The value associated with the key.

        If either key or item is None, this method does nothing.
        If the number of items exceeds MAX_ITEMS, the least recently used
        item is removed and the key is printed in a discard message.
        """
        if key is None or item is None:
            return

        # Add or update the cache with the new key and item
        self.cache_data[key] = item

        # If the number of items exceeds MAX_ITEMS, discard the least recently used
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the first item in the cache (the least recently used)
            lru_key = list(self.cache_data.keys())[0]
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """
        Retrieve an item from the cache by key.

        Args:
            key (str): The key to look for in the cache.

        Returns:
            str: The value associated with the key, or None if the key is not found.
        
        If the key is None or doesn't exist in the cache, returns None.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
