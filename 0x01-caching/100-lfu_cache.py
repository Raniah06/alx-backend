#!/usr/bin/python3
""" LFU Caching System """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class inherits from BaseCaching and implements
    a Least Frequently Used (LFU) caching system.
    """

    def __init__(self):
        """Initialize the class."""
        super().__init__()
        self.usage_frequency = {}  # Tracks frequency of usage
        self.usage_order = {}  # Tracks the order of usage
        self.current_order = 0

    def put(self, key, item):
        """Add an item to the cache with LFU eviction."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the value and frequency
            self.cache_data[key] = item
            self.usage_frequency[key] += 1
            self.usage_order[key] = self.current_order
            self.current_order += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Eviction needed
                lfu_key = self._get_lfu_key()
                del self.cache_data[lfu_key]
                del self.usage_frequency[lfu_key]
                del self.usage_order[lfu_key]
                print(f"DISCARD: {lfu_key}")

            # Add the new item
            self.cache_data[key] = item
            self.usage_frequency[key] = 1
            self.usage_order[key] = self.current_order
            self.current_order += 1

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and order of usage
        self.usage_frequency[key] += 1
        self.usage_order[key] = self.current_order
        self.current_order += 1
        return self.cache_data[key]

    def _get_lfu_key(self):
        """Retrieve the key of the least frequently used item."""
        min_freq = min(self.usage_frequency.values())
        
        candidates = [
    key for key, freq in
    self.usage_frequency.items()
    if freq == min_freq
]

        # If multiple candidates, use the least recently used (LRU) among them
        if len(candidates) > 1:
            lfu_key = min(candidates, key=lambda k: self.usage_order[k])
        else:
            lfu_key = candidates[0]

        return lfu_key
