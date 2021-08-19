"""  
Find the minium number of operations required to convert one string to another
Ex - Distance btw abc and yabd = 2
    Substitute c with d and add a y which amounts to 2 operations


sol build a table 

if str[r - 1] == str[c - 1]: table[r][c] = table[r - 1][c - 1]
else: table[r][c] = 1 + min(table[r][c - 1], table[r - 1][c], table[r - 1][c - 1])

"""

table = """
    "" | y | a | b | d 
"" | 0 | 1 | 2 | 3 | 4
a  | 1 |   |   |   |
b  | 2 |   |   |   |
c  | 3 |   |   |   |
"""

# O(nm) time | o(nm) space
def levenshtein_distance(str1, str2):
    table = [[0 for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]

    table[0][0] = 0

    for col in range(1, len(table[0])):
        table[0][col] = col

    for row in range(1, len(table)):
        table[row][0] = row

    # str1 = columns
    # str2 = rows

    for row in range(1, len(str2) + 1):
        for col in range(1, len(str1) + 1):
            if str2[row - 1] == str1[col - 1]:
                table[row][col] = table[row - 1][col - 1]
            else:
                table[row][col] = 1 + min(
                    table[row][col - 1], table[row - 1][col], table[row - 1][col - 1]
                )

    # row_string = str2
    # col_string = str1

    # spaces = 2

    # print(" " * spaces, '""', end=" " * spaces)

    # for s in col_string:
    #     print(s, end=" " * spaces)

    # for row in range(len(table)):
    #     if row == 0:
    #         print("\n", '""', end=" " * spaces)

    #     else:
    #         print("\n", row_string[row - 1], end=" " * spaces)

    #     for c in table[row]:
    #         print(table[row][c], end=" " * spaces)


levenshtein_distance("abc", "yabd")
