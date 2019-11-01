class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        if not matrix[0]:
            return
        
        rows = set()
        cols = set()
        
        for x in range(0, len(matrix)):
            for y in range(0, len(matrix[0])):
                if not matrix[x][y]:
                    rows.add(x)
                    cols.add(y)
        
        for x in rows:
            for y in range(0, len(matrix[0])):
                matrix[x][y] = 0
        
        for y in cols:
            for x in range(0, len(matrix)):
                matrix[x][y] = 0


# Difficulty: medium
# Key points: 
# I really don't know for this one, though it would be a good idea to look for an O(1) space solution later
