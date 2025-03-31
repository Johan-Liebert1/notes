# String matching algo. Given two strings s1 and s2 figure out whether s1 contains s2


def pattern_maker(substring: str) -> list[int]:
    pattern = [-1 for _ in range(len(substring))]

    i, j = 1, 0

    while i < len(substring):
        if substring[i] == substring[j]:
            # found a pattern, i.e. in the current substring[j:i + 1], some prefix is equal to the suffix

            pattern[i] = j  # found the current character at j

            i += 1
            j += 1

        elif j > 0:
            j = pattern[j - 1] + 1

        else:
            i += 1

    return pattern


def does_match(string: str, substring: str, pattern: "list[int]") -> bool:
    i = 0  # for the original string
    j = 0  # for the substring

    while i + len(substring) - j <= len(string):
        if string[i] == substring[j]:
            if j == len(substring) - 1:
                # reached the end of the substring and the last character matched so we're done
                return True

            i += 1
            j += 1

        elif j > 0:
            # characters didn't match so move j to the found pattern if there is any
            j = pattern[j - 1] + 1  # +1 helps if we go to -1 then we end up at 0
        else:
            # at the first character and since we're finding a substring just move i
            i += 1

    return False


def knuth_morris_pratt(string: str, substring: str):
    return does_match(string, substring, pattern_maker(substring))


string = "ssippi"
pattern = pattern_maker(string)

for i in string:
    print(f"{i:<4}", end="")

print()

for i in pattern:
    print(f"{i:<4}", end="")

print()
