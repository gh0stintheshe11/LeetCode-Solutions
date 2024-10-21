class Solution:
    def findAnswer(self, parents: List[int], s: str) -> List[bool]:
        # step 1: build graph
        graph = defaultdict(list)
        for child, parent in enumerate(parents):
            if parent != -1:
                graph[parent].append(child)

        # step 2: get the string (I call dfs_string) that dfs from root
        dfs_string = ""
        def dfs1(node):
            nonlocal dfs_string

            for child in graph[node]:
                dfs1(child)
            
            dfs_string += s[node]
        
        dfs1(0)

        # step 3: build fundtion is_palindrome_query(l,r) to check palindrome of sub string dfs_string[l:r+1]
        def manacher(s):
            t = '#' + '#'.join(s) + '#'
            n = len(t)
            p = [0] * n
            center = 0
            right = 0
            
            for i in range(n):
                mirror = 2 * center - i
                
                if i < right:
                    p[i] = min(right - i, p[mirror])
                
                while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
                    p[i] += 1
                
                if i + p[i] > right:
                    center = i
                    right = i + p[i]
            
            return p
        
        p = manacher(dfs_string)

        def is_palindrome_query(l, r):
            l = 2 * l + 1
            r = 2 * r + 1
            center = (l + r) // 2
            length = r - l + 1
            
            return p[center] >= length // 2
        
        # step 4: create dfs function to get the start index and the end index of dfs_string in every sub tree 
        # then add the result to result array
        res = [False] * len(s)
        def dfs2(node, start):
            nonlocal res

            end= start
            for child in graph[node]:
                end = dfs2(child, end)
            
            res[node] = is_palindrome_query(start, end)
            return end + 1

        dfs2(0, 0)
        return res