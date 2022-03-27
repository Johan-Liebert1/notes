"""  
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


from pprint import pprint


def params_helper(n: int, string: str, stats: dict[str, int]):
    print(f"{n = }")
    pprint(stats, indent=4)

    if n == 0:
        return string

    if stats["num_open"] < n:
        string += "("
        stats["num_open"] += 1
    elif stats["num_close"] < stats["num_open"]:
        string += ")"
        stats["num_close"] += 1

    return params_helper(n - 1, string, stats)


def generate_parens(n: int):
    stats = {"num_open": 0, "num_close": 0}

    return params_helper(n, "", stats)


print(generate_parens(3))
