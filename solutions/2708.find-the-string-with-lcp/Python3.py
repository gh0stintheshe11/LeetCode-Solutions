class Solution:
    def checkNewLCP(self, lcp: List[List[int]], output: List[str]) -> bool:
        n = len(output)
        for row_index in range(n):
            for col_index in range(n):
                prev_val = lcp[row_index+1][col_index+1] if (row_index+1 < n and col_index+1 < n) else 0
                expected_val = -1
                if output[col_index] == output[row_index]:
                    expected_val = prev_val + 1
                else:
                    expected_val = 0
                if lcp[row_index][col_index] != expected_val:
                    return False
        return True

    def checkOldLCP(self, lcp: List[List[int]]) -> bool:
        n = len(lcp)
        for row_index in range(n):
            for col_index in range(n):
                if row_index == col_index:
                    expected_value = n - row_index
                    if lcp[row_index][col_index] != expected_value:
                        return False
                if lcp[row_index][col_index] != lcp[col_index][row_index]:
                    return False
                if lcp[row_index][col_index] > n - max(row_index, col_index):
                    return False
        return True

    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        if not self.checkOldLCP(lcp):
            return ""
        
        output = ['$'] * n
        current_letter_index = 0

        for row_index in range(n):
            for col_index in range(row_index, n):
                if output[row_index] == '$':
                    if ord('a') + current_letter_index > ord('z'):
                        return ""
                    output[row_index] = chr(ord('a') + current_letter_index)
                    current_letter_index += 1

                assert output[row_index] != '$'
                if lcp[row_index][col_index] == 0:
                    if output[row_index] == output[col_index]:
                        return ""
                else:
                    if output[col_index] != '$':
                        if output[col_index] != output[row_index]:
                            return ""
                    else:
                        output[col_index] = output[row_index]
        
        if not self.checkNewLCP(lcp, output):
            return ""
        else:
            return "".join(output)