class Solution:
    def maxArea(self, height: int, positions: List[int], directions: str) -> int:
        dir_counter = Counter(directions)
        piston_tops = defaultdict(int)
        piston_bottoms = defaultdict(int)
        for p, d in zip(positions, [*directions]):
            if d == "U":
                piston_tops[height - p] += 1
                piston_bottoms[height - p + height] += 1
            else:
                piston_bottoms[p] += 1
                piston_tops[p + height] += 1
        
        end_times = set(piston_tops.keys()).union(piston_bottoms.keys())
        end_times.add(0)

        ans = curr_area = sum(positions)
        
        for t1, t2 in itertools.pairwise(sorted(end_times)):
            timedelta = t2 - t1
            curr_area += (timedelta * dir_counter["U"])
            curr_area -= (timedelta * dir_counter["D"])

            ans = max(ans, curr_area)

            dir_counter["U"] -= piston_tops[t2]
            dir_counter["U"] += piston_bottoms[t2]
            dir_counter["D"] -= piston_bottoms[t2]
            dir_counter["D"] += piston_tops[t2]
            
        return ans