from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    MRUCache class that implements a Most Recently Used (MRU) cache.

    This class inherits from BaseCaching and implements the put and get methods.
    The cache stores key-value pairs and evicts the most recently used item
    when the cache exceeds the maximum allowed items.
    """
    
    def __init__(self):
        """Initialize the MRUCache class."""
        super().__init__()
        self.access_order = []  # Tracks the access order of keys

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
            # Update the item and move the key to the end of access_order
            self.access_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Evict the most recently used item
            mru_key = self.access_order.pop()  # Get the most recently used key
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add or update the cache
        self.cache_data[key] = item
        self.access_order.append(key)  # Mark this key as the most recently used

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

        # Mark the key as the most recently used
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
