class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Choose the order based on the higher score
        if x > y:
            first, second = 'ab', 'ba'
            first_score, second_score = x, y
        else:
            first, second = 'ba', 'ab'
            first_score, second_score = y, x
            
        def remove_and_score(s, sub, score):
            stack = []
            total_score = 0
            for c in s:
                if stack and stack[-1] == sub[0] and c == sub[1]:
                    stack.pop()
                    total_score += score
                else:
                    stack.append(c)
            return "".join(stack), total_score
        
        # First remove the more rewarding substring
        s, score1 = remove_and_score(s, first, first_score)
        # Then remove the other substring
        _, score2 = remove_and_score(s, second, second_score)
        
        return score1 + score2