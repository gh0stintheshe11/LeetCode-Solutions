import random
import functools
from typing import List

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        
        START_NODE = random.randint(0, n-1)
        graph = [list() for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        listChildrenNodes = [list() for _ in range(n)]         
        parentOf = [None]*n

        def populate_tree(currNode = START_NODE, parentNode = None):
            nonlocal graph, parentOf, listChildrenNodes
            if parentNode != None:
                parentOf[currNode] = parentNode
            for childNode in graph[currNode]:
                if childNode != parentNode:
                    populate_tree(childNode, currNode)
                    listChildrenNodes[currNode].append(childNode)
            return
        
        @functools.lru_cache(maxsize = None)
        def get_node_maxpath(currNode = START_NODE):
            if currNode == None:    
                return 0
            currPrice = price[currNode]
            maxPaths = [currPrice]*2
            for childNode in listChildrenNodes[currNode]:
                _, childMaxPath = get_node_maxpath(childNode)
                maxPaths = sorted(maxPaths + [currPrice + childMaxPath])[-2:]
            return maxPaths

        @functools.lru_cache(maxsize = None)
        def get_parent_maxpath(childNode, parentNode):
            if parentNode == None or childNode == None:     
                return 0
            parentMaxPaths = get_node_maxpath(parentNode)
            _, childMaxPath = get_node_maxpath(childNode)
            maxPath = parentMaxPaths[1]
            if childMaxPath + price[parentNode] == parentMaxPaths[1]:
                maxPath = parentMaxPaths[0]
            maxPath = max(maxPath, price[parentNode] + get_parent_maxpath(parentNode, parentOf[parentNode]))
            return maxPath

        def get_node_cost(currNode):
            _, maxPath = get_node_maxpath(currNode)
            return max(maxPath - price[currNode], get_parent_maxpath(currNode, parentOf[currNode]))

        populate_tree()
        maxCost = max(get_node_cost(currNode) for currNode in range(n))
        get_node_maxpath.cache_clear()
        get_parent_maxpath.cache_clear()
        del graph, parentOf, listChildrenNodes

        return maxCost