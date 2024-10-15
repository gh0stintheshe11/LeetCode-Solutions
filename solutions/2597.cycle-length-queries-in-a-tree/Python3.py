class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def find_depth(node):
            depth = 0
            while node > 0:
                node //= 2
                depth += 1
            return depth
        
        def find_LCA(a, b):
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
            return a
        
        answers = []
        for a, b in queries:
            depth_a = find_depth(a)
            depth_b = find_depth(b)
            lca = find_LCA(a, b)
            depth_lca = find_depth(lca)
            cycle_length = (depth_a + depth_b - 2 * depth_lca + 1)
            answers.append(cycle_length)

        return answers