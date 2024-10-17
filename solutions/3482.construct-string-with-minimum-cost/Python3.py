from typing import List, Optional

class Node:
    def __init__(self, cost: Optional[int] = None):
        self.children = {}
        self.cost = cost

class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:

        def build_kmp_prefix() -> List[int]:
            w = [0] * len(target)
            k, i = 0, 1
            while i < len(target):
                if target[i] == target[k]:
                    k += 1
                    w[i] = k
                    i += 1
                else:
                    if k != 0:
                        k = w[k - 1]
                    else:
                        i += 1
            return w

        def find(prefix: List[int], w: str) -> List[List[int]]:
            result = []
            m, n = len(target), len(w)
            i, k = 0, 0
            while i < m:
                if target[i] == w[k]:
                    i += 1
                    k += 1
                if k == n:
                    # Found a match
                    result.append([i - k, i])
                    k = prefix[k - 1]
                elif i < m and target[i] != w[k]:
                    if k != 0:
                        k = prefix[k - 1]
                    else:
                        i += 1
            return result

        target_prefix = build_kmp_prefix()

        root = Node()
        for j, x in enumerate(words):
            if len(x) < 320:
                p = root
                for i in range(len(x)):
                    if x[i] in p.children:
                        p = p.children[x[i]]
                    else:
                        t = Node()
                        p.children[x[i]] = t
                        p = t
                    if i == len(x) - 1:
                        p.cost = min(costs[j], p.cost) if p.cost is not None else costs[j]

        dm = {}
        for i, word in enumerate(words):
            if len(word) >= 320:
                q = find(target_prefix, word)
                for b, e in q:
                    qm = dm.setdefault(e, {})
                    if b in qm:
                        qm[b] = min(qm[b], costs[i])
                    else:
                        qm[b] = costs[i]

        d = [[root, 0]]
        dp = [-1 for _ in range(len(target) + 1)]
        dp[0] = 0
        for i, x in enumerate(target):
            q = []
            t = None
            for p, cost in d:
                if x in p.children:
                    w = p.children[x]
                    if w.cost is not None:
                        t = cost + w.cost if t is None else min(t, cost + w.cost)
                    q.append([w, cost])
            qm = dm.get(i + 1, {})
            for b in qm:
                if dp[b] >= 0:
                    t = dp[b] + qm[b] if t is None else min(t, dp[b] + qm[b])

            if t is not None:
                dp[i + 1] = t
                q.append([root, t])
            d = q

        return dp[len(target)]