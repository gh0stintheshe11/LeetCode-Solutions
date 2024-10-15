class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        # Calculate how much fill is needed in the last segment
        needed_fill = (k - n % k) % k
        # If needed, extend the string with the fill characters
        s += fill * needed_fill
        # Return the divided string into groups of size k
        return [s[i:i + k] for i in range(0, len(s), k)]