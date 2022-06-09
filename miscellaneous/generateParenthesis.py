"""  
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


def generate_parens(n: int):
    stats = {"open": 0, "close": 0}

    all_parens = []

    def recurse(i: int, current_str: list[str]):
        if i == 2 * n:
            all_parens.append("".join(current_str))
            return

        if stats["open"] < n:
            current_str.append("(")
            stats["open"] += 1

            recurse(i + 1, current_str)

            current_str.pop()
            stats["open"] -= 1

        # we can only close and have valid parens if more have opened
        if stats["open"] > stats["close"]:
            current_str.append(")")
            stats["close"] += 1

            recurse(i + 1, current_str)

            current_str.pop()
            stats["close"] -= 1

    recurse(0, [])

    return all_parens


print(generate_parens(8))
