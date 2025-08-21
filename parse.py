took = "Took "


def sort_func(x: str):
    x = x.split(" ")[1]

    if x.endswith("ms"):
        return float(x[:-2]) * 1000

    if x.endswith("s"):
        return float(x[:-2]) * 1000 * 1000

    if x.endswith("µs"):
        return float(x[:-2])

    return -1


with open("./times") as times:
    lines = times.readlines()
    lines = sorted(lines, key=sort_func, reverse=True)

    with open("./sorted-times", "w") as sorted_times:
        sorted_times.write("".join(lines))
