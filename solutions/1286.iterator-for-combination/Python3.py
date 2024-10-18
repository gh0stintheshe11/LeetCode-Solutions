from itertools import combinations

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = list(combinations(characters, combinationLength))
        self.index = 0

    def next(self) -> str:
        result = ''.join(self.combinations[self.index])
        self.index += 1
        return result

    def hasNext(self) -> bool:
        return self.index < len(self.combinations)