class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def permute(newa: str, newb: str, newc: str) -> str:
            ansstr = newa
            
            if not newb in ansstr:
                bsize = len(newb)
                boverlap = False
                for ridx in range(bsize - 1, 0, -1):
                    if ansstr.endswith(newb[:ridx]):
                        ansstr += newb[ridx:]
                        boverlap = True
                        break
                if not boverlap:
                    ansstr += newb
            
            if not newc in ansstr:
                csize = len(newc)
                coverlap = False
                for ridx in range(csize - 1, 0, -1):
                    if ansstr.endswith(newc[:ridx]):
                        ansstr += newc[ridx:]
                        coverlap = True
                        break
                if not coverlap:
                    ansstr += newc
            
            return ansstr
        
        def lexsmaller(test1: str, test2: str) -> str:
            if len(test2) < len(test1):
                return test2
            elif len(test2) == len(test1):
                return min(test1, test2)
            else:
                return test1
        
        ans = permute(a, b, c)
        ans = lexsmaller(ans, permute(a, c, b))
        ans = lexsmaller(ans, permute(b, a, c))
        ans = lexsmaller(ans, permute(b, c, a))
        ans = lexsmaller(ans, permute(c, a, b))
        ans = lexsmaller(ans, permute(c, b, a))

        return ans