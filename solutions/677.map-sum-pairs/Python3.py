class MapSum:

    def __init__(self):
        self.map = {}
        self.prefix_map = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.map.get(key, 0)
        self.map[key] = val

        prefix = ""
        for char in key:
            prefix += char
            if prefix in self.prefix_map:
                self.prefix_map[prefix] += delta
            else:
                self.prefix_map[prefix] = delta

    def sum(self, prefix: str) -> int:
        return self.prefix_map.get(prefix, 0)