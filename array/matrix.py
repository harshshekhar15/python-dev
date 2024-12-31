# Rotate Matrix/ Image - LeetCode 48
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

# DO NOT allocate another 2D matrix and do the rotation.

# Example:

# Input: 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

def rotate(matrix):
    # TODO
    result = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
    print(f'Matrix length: {len(matrix)}')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][len(matrix)-1-i] = matrix[i][j]
    return result

def rotate_optimised(matrix):
    print(f"Initial matrix: {matrix}")
    transpose(matrix)
    print(f"Transposed matrix: {matrix}")
    reverse_rows(matrix=matrix)
    print(f"Rotated matrix: {matrix}")
    return matrix

def transpose(matrix):
    for i in range(0, len(matrix)-1):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse_rows(matrix):
    for i in range(len(matrix)):
        j, k = 0, len(matrix)-1
        while j < k:
            matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
            j += 1
            k -= 1

rotate_optimised(matrix=matrix)