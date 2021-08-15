def go_diag_up(matrix, array, row, col):
    row -= 1
    col += 1
    while row > -1 and col < len(matrix[0]):
        array.append(matrix[row][col])
        row -= 1
        col += 1

    row += 1
    col -= 1

    return row, col


def go_diag_down(matrix, array, row, col):
    row += 1
    col -= 1
    while row < len(matrix) and col > -1:
        array.append(matrix[row][col])
        row += 1
        col -= 1

    col += 1
    row -= 1

    return row, col


def zigzag(matrix):
    array = [matrix[0][0]]
    row, col = 0, 0
    down_or_right = 'r'
    break_out = False

    while row < len(matrix):
        col = 0
        while col < len(matrix[0]):
            if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
                break_out = True
                break

            if down_or_right == 'd' and row == len(matrix) - 1:
                down_or_right = 'r'

            elif down_or_right == 'r' and col == len(matrix[0]) - 1:
                down_or_right = 'd'

            if down_or_right == 'd':
                row += 1
                array.append(matrix[row][col])

                if col == len(matrix[0]) - 1:
                    row, col = go_diag_down(matrix, array, row, col)

                else:
                    row, col = go_diag_up(matrix, array, row, col)

            elif down_or_right == 'r':
                col += 1
                array.append(matrix[row][col])

                if row == len(matrix) - 1:
                    row, col = go_diag_up(matrix, array, row, col)

                else:
                    row, col = go_diag_down(matrix, array, row, col)

            if down_or_right == 'd':
                if not row == len(matrix) - 1:
                    down_or_right = 'r'

            elif down_or_right == 'r':
                if not col == len(matrix[0]) - 1:
                    down_or_right = 'd'

            print(row, col, down_or_right, array)

        if break_out:
            break

    return array


mat = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10],
    [11, 12, 13],
    [14, 15, 16]
]

zig_zagged = zigzag(mat)

print(zig_zagged)
