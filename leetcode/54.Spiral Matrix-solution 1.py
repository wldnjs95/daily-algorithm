# LeetCode 54: Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ROWS, COLS = len(matrix), len(matrix[0])
        res = []

        # track counts
        total = ROWS * COLS
        count = 0

        # start left top corner
        r,c = 0,0
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        current_dir = 0

        while count < total:
            res.append(matrix[r][c])
            matrix[r][c] = float('inf')
            count +=1

            # update coord
            nr,nc = r+dirs[current_dir][0], c+dirs[current_dir][1]
            if 0<=nr<ROWS and 0<=nc<COLS and matrix[nr][nc]!=float('inf'):
                r,c = nr,nc
            else:
                current_dir = (current_dir + 1)%4
                r,c = r+dirs[current_dir][0], c+dirs[current_dir][1]

        
        return res
            

