class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(subs: str) -> bool:
            return subs == subs[::-1]
        
        def dfs(start: int, path: List[str]):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    dfs(end, path + [s[start:end]])
        
        result = []
        dfs(0, [])
        return result