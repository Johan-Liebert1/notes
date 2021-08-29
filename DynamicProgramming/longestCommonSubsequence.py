def lcs_more_space(s1: str, s2: str) -> str:
    table = [["" for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]

    for row in range(1, len(table)):
        for col in range(1, len(table[0])):
            if s2[row - 1] == s1[col - 1]:
                table[row][col] = table[row - 1][col - 1] + s1[col - 1]

            else:
                table[row][col] = max(
                    table[row - 1][col], table[row][col - 1], key=lambda x: len(x)
                )
    for row in table:
        print(row)
    return table[-1][-1]


def lcs_less_space(s1: str, s2: str) -> str:
    # None1 = are we using the current character in the lcs
    # 0 = length of the current lcs
    # None2 = which row did we come from
    # None3 = which column did we come from

    table = [
        [[None, 0, None, None] for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)
    ]

    for row in range(1, len(table)):
        for col in range(1, len(table[0])):
            if s2[row - 1] == s1[col - 1]:
                table[row][col] = [
                    True,
                    table[row - 1][col - 1][1] + 1,
                    row - 1,
                    col - 1,
                ]

            else:
                if table[row - 1][col][1] > table[row][col - 1][1]:
                    table[row][col] = [None, table[row - 1][col][1], row - 1, col]

                else:
                    table[row][col] = [None, table[row][col - 1][1], row, col - 1]

    lcs = ""

    row, col = len(table) - 1, len(table[0]) - 1

    while table[row][col][2] is not None:
        letter_used, _, prev_row, prev_col = table[row][col]

        if letter_used:
            lcs += s1[col - 1]

        row = prev_row
        col = prev_col

    print(lcs[::-1])

    for row in table:
        print(row)


# lcs_more_space("ab", "abc")
lcs_less_space("ab", "abc")
