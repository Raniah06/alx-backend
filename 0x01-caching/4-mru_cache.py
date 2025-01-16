from collections import OrderedDict
from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """MRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache, evicting the most recently used item if necessary"""
        if key is None or item is None:
            return
        if key in self.cache:
            # Move the key to the end (most recent)
            self.cache.move_to_end(key)
        self.cache[key] = item

        if len(self.cache) > BaseCaching.MAX_ITEMS:
            # Pop the first (least recently used) item
            discarded_key, discarded_value = self.cache.popitem(last=False)
            print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """Return the value linked to the key, or None if the key does not exist"""
        if key is None or key not in self.cache:
            return None
        # Move the key to the end (most recent)
        self.cache.move_to_end(key)
        return self.cache[key]

    def print_cache(self):
        """Print the current state of the cache"""
        print("Current cache:")
        for key, value in self.cache.items():
            print(f"{key}: {value}")
