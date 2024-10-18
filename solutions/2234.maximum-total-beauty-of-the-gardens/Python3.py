class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        totf = 0
        for i, f in enumerate(flowers):
            if f > target:
                flowers[i] = target
            totf += min(f, target)
        flowers.sort(reverse=True)
        
        # if newFlowers can make all garden 'full'
        n = len(flowers)
        if n * target - totf <= newFlowers:
            maxscore = n * full  # score if all garden 'full'
            if flowers[-1] < target:  # score if all garden but one 'full'
                maxscore = max(maxscore, (n - 1) * full + (target - 1) * partial) 
            return maxscore
        
        # if newFlowers can not make all garden 'full'
        tofill = 0  # no garden full, n gardens to fill
        level = (totf + newFlowers) // (n - tofill)  # try fill all n garden
        while level < flowers[tofill]:  # not plausible
            totf -= flowers[tofill]  # exclude the next garden
            tofill += 1
            level = (totf + newFlowers) // (n - tofill)  # try again
        maxscore = level * partial  # score if no garden 'full'
        for i in range(len(flowers)):  # (i+1) 'garden full'
            newFlowers -= target - flowers[i] 
            if newFlowers < 0:  # cannot fill any more garden
                break
            score = (i + 1) * full  # score from (i+1) 'full' garden
            if tofill == i:
                totf -= flowers[i]
                tofill = i + 1
            level = (totf + newFlowers) // (n - tofill)  # try fill the rest of the gardens
            while level < flowers[tofill]:  # not plausible
                totf -= flowers[tofill]  # exclude the next garden
                tofill += 1
                level = (totf + newFlowers) // (n - tofill)
            score = score + level * partial  # score from partial gardens
            if score > maxscore:
                maxscore = score
        return maxscore