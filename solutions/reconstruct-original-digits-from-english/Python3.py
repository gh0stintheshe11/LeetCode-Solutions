from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        out = {}
        
        # Identify the unique characters for each number
        out['0'] = count['z']
        out['2'] = count['w']
        out['4'] = count['u']
        out['6'] = count['x']
        out['8'] = count['g']
        out['1'] = count['o'] - out['0'] - out['2'] - out['4']
        out['3'] = count['h'] - out['8']
        out['5'] = count['f'] - out['4']
        out['7'] = count['s'] - out['6']
        out['9'] = count['i'] - out['5'] - out['6'] - out['8']
        
        # Build the result based on the identified counts
        result = []
        for num in sorted(out.keys()):
            result.append(num * out[num])
            
        return ''.join(result)