from collections import defaultdict
from typing import List

class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        graph = defaultdict(list)
        eq = {}
        for i in range(len(equations)):
            graph[equations[i][0]].append(equations[i][1])
            graph[equations[i][1]].append(equations[i][0])
            if (equations[i][0],equations[i][1]) in eq.keys():
                if abs(eq[(equations[i][0],equations[i][1])]-values[i])>pow(10,-5):
                    return True
            if (equations[i][1],equations[i][0]) in eq.keys():
                if abs(eq[(equations[i][1],equations[i][0])]-1/values[i])>pow(10,-5):
                    return True
            eq[(equations[i][0],equations[i][1])]=values[i]
            eq[(equations[i][1],equations[i][0])]=1/values[i]
        def check(a,b,v,seen):
            if a==b and abs(v-1)>pow(10,-5):
                return True
            if (a,b) in eq.keys() and abs(v-eq[(a,b)])>pow(10,-5):
                return True
            for c in graph[b]:
                if c not in seen:
                    seen.add(c)
                    return check(a,c,v*eq[(b,c)],seen)
        
        for key in graph.keys():
            seen = set()
            for key1 in graph[key]:
                if check(key,key1,eq[(key,key1)],seen):
                    return True
        return False