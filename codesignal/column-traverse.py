# Problem
# How to traverse a 2x2 matrix column-wise

def column_traverse(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    row, col = ROWS -1, COLS -1
    direction = -1
    output = []
    
    for _ in range(rows * cols):
        output.append(matrix[row][col])
        if direction == -1 or row ==0 or direction == 1 and row == rows -1:
            col -=1
            direction *= -1
        else:
            row += direction
    return output

# test data

bookshelf = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print(column_traverse(bookshelf))