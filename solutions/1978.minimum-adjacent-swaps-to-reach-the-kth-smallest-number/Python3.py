class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        def next_permutation(seq):
            seq = list(seq)
            i = j = len(seq) - 1
            while i > 0 and seq[i - 1] >= seq[i]:
                i -= 1
            if i == 0:
                return False
            while seq[j] <= seq[i - 1]:
                j -= 1
            seq[i - 1], seq[j] = seq[j], seq[i - 1]
            seq[i:] = reversed(seq[i:])
            return seq

        # Initial num for transformation
        original = list(num)

        # Generate the kth permutation
        for _ in range(k):
            num = next_permutation(num)

        # Compare with original and count swaps needed
        target = num
        original = list(original)
        swaps = 0

        for i in range(len(original)):
            if original[i] != target[i]:
                j = i
                while original[j] != target[i]:
                    j += 1
                while j > i:
                    original[j], original[j - 1] = original[j - 1], original[j]
                    j -= 1
                    swaps += 1
        return swaps