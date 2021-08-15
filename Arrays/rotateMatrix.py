def printMatrix(m):
    for row in m:
        print(row)

def transpose(mat):
    for i in range(len(mat)):
        for j in range(i, len(mat)):
            temp = mat[i][j]
            mat[i][j] = mat[j][i]
            mat[j][i] = temp
            

def rotateMatrix(mat):
    transpose(mat)

    for row in mat:
        for i in range(len(row) // 2):
            temp = row[i]
            row[i] = row[len(row) - 1 - i]
            row[len(row) - 1 - i] = temp


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


rotateMatrix(matrix)

printMatrix(matrix)

"""
Note: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 104.

[output] array.array.integer
"""
