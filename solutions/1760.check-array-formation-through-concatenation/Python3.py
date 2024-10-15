class Solution:
    def canFormArray(self, arr, pieces):
        piece_dict = {piece[0]: piece for piece in pieces}
        result = []
        
        i = 0
        while i < len(arr):
            if arr[i] in piece_dict:
                result += piece_dict[arr[i]]
                i += len(piece_dict[arr[i]])
            else:
                return False
        
        return result == arr