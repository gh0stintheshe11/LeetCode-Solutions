from collections import defaultdict
from typing import List

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # Build the directory tree
        class TrieNode:
            def __init__(self):
                self.children = defaultdict(TrieNode)
                self.serial = None

        root = TrieNode()

        def insert_path(path):
            node = root
            for folder in path:
                node = node.children[folder]

        for path in paths:
            insert_path(path)

        serial_to_node = defaultdict(list)

        # Serialize the folder structure using DFS
        def serialize(node):
            if not node.children:
                return ""
            serials = []
            for child in sorted(node.children.keys()):  # Sort for consistent serialization
                child_serial = serialize(node.children[child])
                serials.append(child + "(" + child_serial + ")")
            node.serial = "".join(serials)
            serial_to_node[node.serial].append(node)
            return node.serial

        serialize(root)

        # Mark nodes for deletion which have the same serialization
        to_delete = set()
        for nodes in serial_to_node.values():
            if len(nodes) > 1:
                to_delete.update(nodes)

        result = []

        # Collect all paths except those marked for deletion
        def collect_paths(node, path):
            if node in to_delete:
                return
            if path:
                result.append(path[:])
            for folder in node.children:
                path.append(folder)
                collect_paths(node.children[folder], path)
                path.pop()

        collect_paths(root, [])

        return result