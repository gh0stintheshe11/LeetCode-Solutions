class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        from collections import defaultdict
        content_to_paths = defaultdict(list)
        
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            for file in parts[1:]:
                file_name, content = file.split("(")
                content = content[:-1]  # Remove the trailing ')'
                content_to_paths[content].append(f"{directory}/{file_name}")
        
        return [group for group in content_to_paths.values() if len(group) > 1]