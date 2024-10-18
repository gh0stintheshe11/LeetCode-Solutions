class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        def backtrack(start_idx, sequence):
            if start_idx == len(num) and len(sequence) >= 3:
                return sequence
            
            current_num = 0
            for i in range(start_idx, len(num)):
                if i > start_idx and num[start_idx] == '0':
                    break
                
                current_num = current_num * 10 + int(num[i])
                
                if current_num > (1 << 31) - 1:
                    break

                if len(sequence) < 2 or current_num == sequence[-1] + sequence[-2]:
                    sequence.append(current_num)
                    result = backtrack(i + 1, sequence)
                    if result:
                        return result
                    sequence.pop()
                elif len(sequence) >= 2 and current_num > sequence[-1] + sequence[-2]:
                    break
            
            return []
        
        return backtrack(0, [])