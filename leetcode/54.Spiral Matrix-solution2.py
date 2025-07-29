class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS-1
        left, right = 0, COLS-1

        while top <= bottom and left <= right:

            # top row (moving right)
            if top <= bottom:
                for i in range(left, right + 1):
                    res.append(matrix[top][i])
                top += 1

            # right column (moving down)
            if left <= right:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][right])
                right -= 1

            # bottom row (moving left)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            # left column (moving up)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res