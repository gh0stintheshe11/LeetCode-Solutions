from sortedcontainers import SortedList

class fenwick(object):
    def __init__(self, n):
        self.n = n
        self.cul = [0] * n
        self.maxd = len(bin(n)) - 3

    def update(self, index, diff):
        i = index
        while i < self.n:
            self.cul[i] += diff
            i += (i + 1) & (-i - 1)

    def getaccu(self, index):
        output = 0
        i = index
        while i >= 0:
            output += self.cul[i]
            i -= (i + 1) & (-i - 1)
        return output

class Solution:
    def numberOfAlternatingGroups(self, colors, queries):
        n = len(colors)
        blocks = SortedList()

        fencount = fenwick(n + 1)
        fentot = fenwick(n + 1)

        ans = []

        def update(index, flag):
            if flag:
                if len(blocks) == 1:
                    blocks.clear()
                    return

                loc = blocks.bisect_left(index)
                if loc == 0:
                    left = blocks[-1] - n
                else:
                    left = blocks[loc - 1]
                
                if loc == len(blocks) - 1:
                    right = blocks[0] + n
                else:
                    right = blocks[loc + 1]

                fentot.update(right - left, (right - left))
                fencount.update(right - left, 1)
                
                fentot.update(index - left, -(index - left))
                fencount.update(index - left, -1)
                
                fentot.update(right - index, -(right - index))
                fencount.update(right - index, -1)

                blocks.pop(loc)
                
            else:
                if len(blocks) == 0:
                    blocks.add(index)
                    return

                loc = blocks.bisect_left(index)
                if loc == 0:
                    left = blocks[-1] - n
                else:
                    left = blocks[loc - 1]
                    
                if loc == len(blocks):
                    right = blocks[0] + n
                else:
                    right = blocks[loc]
                    
                fentot.update(right - left, -(right - left))
                fencount.update(right - left, -1)
                
                fentot.update(index - left, (index - left))
                fencount.update(index - left, 1)
                
                fentot.update(right - index, (right - index))
                fencount.update(right - index, 1)
                
                blocks.add(index)

        fentot.update(n, n)
        fencount.update(n, 1)

        for i in range(n):
            if colors[i] == colors[i - 1]:
                update(i, False)

        for ele in queries:
            if len(ele) == 2:
                l = ele[1]
                if len(blocks) == 0:
                    ans.append(n)
                    continue

                count = fencount.getaccu(n) - fencount.getaccu(l - 1)
                tot = fentot.getaccu(n) - fentot.getaccu(l - 1)
                ans.append(tot - count * (l - 1))
                
            else:
                index = ele[1]
                c = ele[2]
                
                if colors[index] == c:
                    continue
                
                if colors[index] == colors[index - 1]:
                    update(index, True)
                else:
                    update(index, False)
                    
                if colors[index] == colors[(index + 1) % n]:
                    update((index + 1) % n, True)
                else:
                    update((index + 1) % n, False)
                    
                colors[index] = c
                
        return ans