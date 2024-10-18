class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        from collections import Counter
        hand_count = Counter(hand)
        
        for key in sorted(hand_count):
            if hand_count[key] > 0:
                need = hand_count[key]
                for i in range(key, key + groupSize):
                    if hand_count[i] < need:
                        return False
                    hand_count[i] -= need
                    
        return True