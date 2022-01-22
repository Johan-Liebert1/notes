def isValidSudoku(board) -> bool:
    for i in board:
        print(i)

    print()

    for row in range(len(board)):
        mapping1 = {}
        mapping2 = {}
        for col in range(len(board)):
            if board[row][col] == ".":
                continue

            if board[row][col] in mapping1:
                return False

            mapping1[board[row][col]] = True

            print(f"{mapping1=}")

            if board[col][row] == ".":
                continue

            if board[col][row] in mapping2:
                return False

            mapping2[board[col][row]] = True

            print(f"{mapping2=}")

    # check boxes
    for row in range(0, len(board), 3):
        for col in range(0, len(board), 3):
            # actual checking starts
            mapping = {}

            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    if board[i][j] == ".":
                        continue

                    if board[i][j] in mapping:
                        return False

                    mapping[board[i][j]] = True

    return True


isValidSudoku(
    [
        [".", ".", "4", ".", ".", ".", "6", "3", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ["5", ".", ".", ".", ".", ".", ".", "9", "."],
        [".", ".", ".", "5", "6", ".", ".", ".", "."],
        ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
        [".", ".", ".", "7", ".", ".", ".", ".", "."],
        [".", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ]
)
