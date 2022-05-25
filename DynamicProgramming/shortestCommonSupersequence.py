class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> str:
        table = [
            [[None, 0, None, None] for _ in range(len(s1) + 1)]
            for _ in range(len(s2) + 1)
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

        return lcs[::-1]

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        lcs = self.longestCommonSubsequence(str1, str2)

        scs = ""

        p1, p2, pl = 0, 0, 0

        while pl < len(lcs):
            # if the character is in lcs then we only want to include it once
            while p1 < len(str1) and str1[p1] != lcs[pl]:
                scs += str1[p1]
                p1 += 1

            while p2 < len(str2) and str2[p2] != lcs[pl]:
                scs += str2[p2]
                p2 += 1

            scs += lcs[pl]
            pl += 1
            p1 += 1
            p2 += 1

        print(f"{p1 = }, {p2 = }, {lcs = }")

        if p1 < len(str1):
            scs += str1[p1:]

        if p2 < len(str2):
            scs += str2[p2:]

        return scs
