from collections import defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_map = {}
        self.freq_map = defaultdict(dict)
        self.key_freq = {}
        
    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        
        # Get current value and frequency of the key
        value = self.key_map[key]
        freq = self.key_freq[key]
        
        # Update the frequency of the key
        del self.freq_map[freq][key]
        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if self.min_freq == freq:
                self.min_freq += 1
                
        self.key_freq[key] = freq + 1
        self.freq_map[freq + 1][key] = value
        
        return value
    
    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.key_map:
            # Update the key value and frequency
            self.key_map[key] = value
            self.get(key)  # This will update frequency internally
        else:
            if len(self.key_map) >= self.capacity:
                # Evict the least frequently used key
                old_key, old_value = next(iter(self.freq_map[self.min_freq].items()))
                del self.freq_map[self.min_freq][old_key]
                if not self.freq_map[self.min_freq]:
                    del self.freq_map[self.min_freq]
                del self.key_map[old_key]
                del self.key_freq[old_key]
            
            # Insert the new key-value pair
            self.key_map[key] = value
            self.key_freq[key] = 1
            self.freq_map[1][key] = value
            self.min_freq = 1