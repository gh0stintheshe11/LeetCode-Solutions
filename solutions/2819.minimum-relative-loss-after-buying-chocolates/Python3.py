import bisect
from typing import List

class Solution:
    def minimumRelativeLosses(self, prices: List[int], queries: List[List[int]]) -> List[int]:
        prices.sort()
        left_sum_arr = [0 for _ in range(len(prices)+1)]
        right_sum_arr = [0 for _ in range(len(prices)+1)]
        left_sum_arr[0] = 0
        right_sum_arr[0] = 0
        for i in range(1, len(left_sum_arr)):
            left_sum_arr[i] = left_sum_arr[i-1]+prices[i-1]
        for i in range(1,len(right_sum_arr)):
            right_sum_arr[i] = right_sum_arr[i-1] + prices[len(prices)-i]
        def scoreCalc(cur_k, total_k, target_score,i,j):
            if cur_k <i or cur_k>j:
                return float("inf")
                
            return left_sum_arr[cur_k] - (right_sum_arr[total_k-cur_k]-target_score*(total_k-cur_k)) + target_score*(total_k-cur_k) 

        res_final = []
        for q in queries:
            max_k = bisect.bisect_left(prices,q[0]+1)
            i = max(0,q[1]-(len(prices)-max_k))
            j = max_k
            i = min(i, q[1])
            j = min(j, q[1])
            while i<=j:
                cur_k = int((i+j)/2)
                cur_score = scoreCalc(cur_k, q[1], q[0],i,j)
                if scoreCalc(cur_k+1, q[1],q[0],i,j)<cur_score:
                    i = cur_k+1
                elif scoreCalc(cur_k-1, q[1],q[0],i,j)<cur_score:
                    j = cur_k-1
                else:
                    break
            res_final.append(cur_score)         
        return res_final