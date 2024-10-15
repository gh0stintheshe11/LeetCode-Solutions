class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i, citation in enumerate(citations):
            if i < citation:
                h_index += 1
            else:
                break
        return h_index