class Solution:
  def colorRed(self, n: int) -> List[List[int]]:
    ans = []
    tipSize = n % 4

    if tipSize >= 1:
      ans.append([1, 1])

    for i in range(2, tipSize + 1):
      ans.append([i, 1])
      ans.append([i, 2 * i - 1])

    for i in range(tipSize + 1, n, 4):
      ans.append([i, 1])

      for j in range(1, i + 1):
        ans.append([i + 1, 2 * j + 1])
      ans.append([i + 2, 2])
      
      for j in range(i + 2 + 1):
        ans.append([i + 3, 2 * j + 1])

    return ans