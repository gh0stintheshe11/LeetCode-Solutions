class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        from collections import Counter
        import heapq
        
        # Count frequency of each character
        count = Counter(s)
        
        # Max Heap (we use negative because Python has a min-heap by default)
        maxHeap = []
        for char, freq in count.items():
            heapq.heappush(maxHeap, (-ord(char), char, freq))
        
        result = []
        
        while maxHeap:
            # Get the largest character available
            _, char, freq = heapq.heappop(maxHeap)

            # Determine how many of this character we can use
            use = min(freq, repeatLimit)

            # Append that many to the result
            result.append(char * use)
            remaining = freq - use

            # Check if there's still occurrence of this character left
            if remaining > 0:
                # Check if there is a different character available
                if not maxHeap:
                    break
                # Get the second largest character
                _, next_char, next_freq = heapq.heappop(maxHeap)
                
                # Append one occurrence of the next largest character
                result.append(next_char)
                next_freq -= 1
                
                # If there's more of the next_char, push it back to the heap
                if next_freq > 0:
                    heapq.heappush(maxHeap, (-ord(next_char), next_char, next_freq))
                
                # Push the remaining of char back to the heap
                heapq.heappush(maxHeap, (-ord(char), char, remaining))
        
        return ''.join(result)