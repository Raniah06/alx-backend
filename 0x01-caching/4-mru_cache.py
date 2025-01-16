#!/usr/bin/python3
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    def __init__(self):
        """Initialize the MRUCache class"""
        super().__init__()

    def put(self, key, item):
        """Assign the value to the dictionary and apply MRU cache logic"""
        if key is None or item is None:
            return

        # Add or update the cache with the new key and item
        self.cache_data[key] = item

        # If the number of items exceeds MAX_ITEMS, discard the most recently used
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the most recently added (last one)
            mru_key = list(self.cache_data.keys())[-1]
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

    def get(self, key):
        """Return the item associated with the key, or None if not found"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
