# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

class Solution:
    def guessMajority(self, reader: 'ArrayReader') -> int:
        counter = [1, 0]
        n = reader.length()
        zeroidx, oneidx = 3, -1
        for i in range(4, n):
            if reader.query(0,1,2,3) == reader.query(0,1,2,i):
                counter[0] += 1
            else:
                counter[1] += 1
                oneidx = i 
        whole = [0,1,2,3,4]
        for i in range(3):
            whole.remove(i)
            if reader.query(0,1,2,4) == reader.query(*whole):
                counter[0] += 1
            else:
                counter[1] += 1
                oneidx = i
            whole.append(i)
            whole.sort()
        print(counter)
        return -1 if counter[0] == counter[1] else (3 if counter[0] > counter[1] else oneidx)

        
            