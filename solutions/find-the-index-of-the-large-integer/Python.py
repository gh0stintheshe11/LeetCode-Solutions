class ArrayReader:
    def compareSub(self, l, r, x, y):
        """
        :type l: int
        :type r: int
        :type x: int
        :type y: int
        :rtype: int
        """
        pass

    def length(self):
        """
        :rtype: int
        """
        pass

class Solution(object):
    def getIndex(self, reader):
        """
        :type reader: ArrayReader
        :rtype: integer
        """
        left, right = 0, reader.length() - 1
        
        while left < right:
            mid = (left + right) // 2
            if (right - left + 1) % 2 == 0:
                # Even number of elements
                result = reader.compareSub(left, mid, mid + 1, right)
                if result == 1:
                    right = mid
                else:
                    left = mid + 1
            else:
                # Odd number of elements
                result = reader.compareSub(left, mid, mid, right)
                if result == 1:
                    right = mid
                else:
                    left = mid
        
        return left