from typing import List


def traverse_row(
    matrix: List[int][int], row: int, start: int, end: int, array: List[int]
):
    for col in range(start, end + 1):
        array.append(matrix[row][col])


def traverse_col(
    matrix: List[int][int], col: int, start: int, end: int, array: List[int]
):
    for row in range(start, end + 1):
        array.append(matrix[row][col])


def spiralTraverse(matrix):
    array: List[int] = []

    start_row = 0
    end_row = len(matrix) - 1
    start_col = 0
    end_col = len(matrix[0]) - 1

    total_rows = len(matrix)
    total_cols = len(matrix[0])
    total_elements = total_rows * total_cols

    while len(array) < total_elements:
        traverse_row(matrix, start_row, start_col, end_col, array)

        start_col = end_col
        start_row += 1

        traverse_col(
            matrix,
            start_col,
        )


print(spiralTraverse([[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]))
