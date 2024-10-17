class Solution:
    def minimumLines(self, points: List[List[int]]) -> int:

      @lru_cache(None)
      def helper(tups):
        if len(tups) == 0: return 0
        elif len(tups) <= 2: return 1
        else:
          slope_dict = {}
          for i in range(len(tups)):
            s_x, s_y = points[tups[i]]
            for j in range(i+1, len(tups)):
              t_x, t_y = points[tups[j]]
              slope = None
              const = None
              if s_x == t_x:
                slope = "inf"
                const = s_x
              else:
                slope = (s_y - t_y)*1.0/(s_x - t_x)
                const = s_y - slope*s_x
              if (slope, const) not in slope_dict:
                slope_dict[(slope, const)] = set()
                slope_dict[(slope, const)].add(tups[i])
                slope_dict[(slope, const)].add(tups[j])
              else:
                slope_dict[(slope, const)].add(tups[i])
                slope_dict[(slope, const)].add(tups[j])
          maxi = -sys.maxsize
          track = None
          for key, value in slope_dict.items():
            if len(value) > maxi:
              maxi = len(value)
              track = [key]
            elif len(value) == maxi:
              track.append(key)
          best = sys.maxsize
          for element in track:
            new_points = []
            for t in range(len(tups)):
              if tups[t] not in slope_dict[element]:
                new_points.append(tups[t])
            new_tups = tuple(new_points)
            best = min(best, helper(new_tups))
          return best + 1
        
      return helper(tuple([i for i in range(len(points))]))