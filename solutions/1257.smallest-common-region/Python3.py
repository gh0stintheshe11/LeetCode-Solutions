class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = {}
        for region in regions:
            root = region[0]
            for sub_region in region[1:]:
                parent[sub_region] = root

        def find_ancestors(region):
            ancestors = []
            while region in parent:
                ancestors.append(region)
                region = parent[region]
            ancestors.append(region) # add root
            return ancestors
        
        ancestors1 = find_ancestors(region1)
        ancestors2 = find_ancestors(region2)
        
        set_ancestors2 = set(ancestors2)
        for ancestor in ancestors1:
            if ancestor in set_ancestors2:
                return ancestor