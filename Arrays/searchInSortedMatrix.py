# rows sorted from left to right
# cols sorted from top to down

def search_in_sorted_matrix(matrix, target):
    row, col = 0, 0

    while row < len(matrix):
        number = matrix[row][col]

        if number == target:
            return True

        if target > number:
            col += 1

        elif target < number:
            return False

        if col == len(matrix[0]):
            col = 0
            row += 1

    return False


mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
t = 13

print(search_in_sorted_matrix(mat, t))
