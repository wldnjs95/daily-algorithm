# Utilizing list comprehension to reflect a square matrix over its secondary diagonal

def reflectOverSecondaryDiagonal(matrix):
    size = len(matrix)
    return [[matrix[size-j-1][size-i-1] for j in range(size)] for i in range(size)]
# Example square matrix to reflect over the secondary diagonal
square_matrix = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]



# Call the function and print the transformed matrix
transformed_matrix = reflectOverSecondaryDiagonal(square_matrix)
# TODO: Call the function on square_matrix and store the result in transformed_matrix.
print(transformed_matrix)
# Output should be:
# [
#  [9, 6, 3],
#  [8, 5, 2],
#  [7, 4, 1]
# ]