"""  
Given a string s, determine the minimum number of cuts required in the strings, so that every 
substring between the cuts is a palindrome.

Example 

Input - noonabbad
Cuts (output) - 2

noon | abba | d <- the cuts
"""

# Time : O(n^3)
def get_palindrome_matrix(string: str):
    """
    function will return a matrix

    index i,j of the matrix is either true or false

    matrix[i][j] = whether the substring starting from i to j is a palindrome or not
    """

    matrix: "list[list[bool]]" = [
        [None for _ in range(len(string))] for _ in range(len(string))
    ]

    for i in range(len(string)):
        for j in range(i, len(string)):
            matrix[i][j] = string[i : j + 1] == string[i : j + 1][::-1]

    # for r in matrix:
    #     print(r)

    return matrix


# Time : O(n^2)
def get_better_palindrome_matrix(string: str):
    matrix: "list[list[bool]]" = [
        [None for _ in range(len(string))] for _ in range(len(string))
    ]

    for i in range(len(string)):
        matrix[i][i] = True  # the diagonals, i.e. just a single letter

    for substring_length in range(2, len(string) + 1):
        for i in range(0, len(string) - substring_length + 1):
            j = i + substring_length - 1

            if substring_length == 2:
                matrix[i][j] = string[i] == string[j]

            else:
                matrix[i][j] = string[i] == string[j] and matrix[i + 1][j - 1]

    return matrix


def palindrome_partitioning(string: str):
    palindromes = get_better_palindrome_matrix(string)

    """  
    iterate through the string and at every index, check if the substring till that 
    index is a palindrome, if it is then the min number of cuts until that index is 0.

    if it's not a palindrome, then starting from the beginning, iterate through the string 
    again to check if a new palindrome was formed by the addition of the current letter than 
    we're on
    """

    cuts = [-1 for _ in range(len(string))]

    for i in range(len(string)):
        if palindromes[0][i]:
            # the string upto the current index is a palindrome
            cuts[i] = 0
            continue

        tentative_cuts = cuts[i - 1] + 1

        for j in range(1, i + 1):
            if palindromes[j][i]:
                tentative_cuts = min(cuts[j - 1] + 1, tentative_cuts)

        cuts[i] = tentative_cuts

    print(cuts)


palindrome_partitioning("noonabbad")
