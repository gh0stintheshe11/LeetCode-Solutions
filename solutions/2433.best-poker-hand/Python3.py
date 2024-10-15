class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"
        
        from collections import Counter
        
        rank_count = Counter(ranks)
        
        if rank_count.most_common(1)[0][1] >= 3:
            return "Three of a Kind"
        
        if rank_count.most_common(1)[0][1] == 2:
            return "Pair"
        
        return "High Card"