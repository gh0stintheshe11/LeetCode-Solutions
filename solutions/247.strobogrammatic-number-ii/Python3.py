class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def build_pairs(length):
            if length == 0:
                return [""]
            if length == 1:
                return ["0", "1", "8"]
            
            middles = build_pairs(length - 2)
            result = []
            for middle in middles:
                if length != n:
                    result.append("0" + middle + "0")
                result.append("1" + middle + "1")
                result.append("6" + middle + "9")
                result.append("8" + middle + "8")
                result.append("9" + middle + "6")
            return result
        
        return build_pairs(n)