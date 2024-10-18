class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [-1] * n
        
        for node in range(n):
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if parent[child] != -1:
                        return False
                    parent[child] = node
        
        root_count = 0
        for node in range(n):
            if parent[node] == -1:
                root_count += 1
                root = node
        
        if root_count != 1:
            return False
        
        visited = [False] * n
        
        def dfs(node):
            if node == -1:
                return True
            if visited[node]:
                return False
            visited[node] = True
            return dfs(leftChild[node]) and dfs(rightChild[node])
        
        if not dfs(root):
            return False
        
        return all(visited)