class MyHashSet:

    def __init__(self):
        self.bucket_count = 769  # A prime number for better distribution
        self.buckets = [[] for _ in range(self.bucket_count)]

    def _hash(self, key: int) -> int:
        return key % self.bucket_count

    def add(self, key: int) -> None:
        bucket_idx = self._hash(key)
        if key not in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].append(key)

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        if key in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].remove(key)

    def contains(self, key: int) -> bool:
        bucket_idx = self._hash(key)
        return key in self.buckets[bucket_idx]