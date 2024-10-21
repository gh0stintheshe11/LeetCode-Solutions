class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        
        for op in operations:
            if op == "C":
                if scores:
                    scores.pop()
            elif op == "D":
                if scores:
                    scores.append(2 * scores[-1])
            elif op == "+":
                if len(scores) >= 2:
                    scores.append(scores[-1] + scores[-2])
            else:
                scores.append(int(op))
        
        return sum(scores)
