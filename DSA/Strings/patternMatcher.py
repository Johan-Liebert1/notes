"""
Given a pattern "xxyxxy" and a string "heyheysamuraiheartheyheysamuraiheart" figure out whether 
the pattern matches the string or not. In this case it does if we assign x = hey and y = samuraiheart
"""


def patten_matcher(pattern: str, string: str):
    num_x, num_y, first_y_position = 0, 0, -1

    for (i, p) in enumerate(pattern):
        if p == "x":
            num_x += 1

        if p == "y":
            num_y += 1

            if first_y_position == -1:
                first_y_position = i

    for (i, s) in enumerate(string):
        x = string[: i + 1]
        y = ""

        if num_y != 0:
            len_y = (len(string) - num_x * len(x)) // num_y
            start_y = len(x) * first_y_position
            y = string[start_y : start_y + len_y]

        generated_string = ""

        for p in pattern:
            generated_string += x if p == "x" else y

        if generated_string == string:
            return True

    return False


print(patten_matcher("xxyxxy", "heyheysamuraiheartheyheysamuraiheart"))
print(patten_matcher("xxxxxx", "heyheyheyheyheyhey"))
print(patten_matcher("xxxxxy", "heyheyheyheyheyhey"))
