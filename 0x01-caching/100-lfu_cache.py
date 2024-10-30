#!/usr/bin/env python3
"""Least Frequently Used caching module"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Represents an object that allows storing and
    retrieving items from a dictionary with a LFU
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """Initializes the cache"""
        super().__init__()
        self.frequency = {}
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                least_frequent_keys = [
                    k for k, freq in self.frequency.items() if freq == min_freq
                ]

                if len(least_frequent_keys) > 1:
                    for k in self.usage_order:
                        if k in least_frequent_keys:
                            del_key = k
                            break
                else:
                    del_key = least_frequent_keys[0]

                del self.cache_data[del_key]
                del self.frequency[del_key]
                del self.usage_order[del_key]

                print(f"DISCARD: {del_key}")

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = None

    def get(self, key):
        """Retrieves an item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]
