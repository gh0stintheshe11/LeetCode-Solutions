class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
            
        def generate(min_val, max_val):
            if min_val > max_val:
                return [None,]

            all_possible_trees = []
            
            for i in range(min_val, max_val + 1):
                left_trees = generate(min_val, i - 1)
                right_trees = generate(i + 1, max_val)
                
                for l in left_trees:
                    for r in right_trees:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        all_possible_trees.append(node)
            
            return all_possible_trees

        return generate(1, n)