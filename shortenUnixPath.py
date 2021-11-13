"""
given - /foo/../test/../test/../foo//bar/./baz
.. -> went up a dir 
. -> in the same dir

op -> /foo/bar/baz
"""


def parser(path: str) -> "list[str]":
    prev_slash_pos = 0
    current_slash_pos = 0

    paths = []

    for i in range(1, len(path)):
        char = path[i]

        if char == "/":
            current_slash_pos = i
            paths.append(path[prev_slash_pos + 1 : current_slash_pos])
            prev_slash_pos = current_slash_pos

    if current_slash_pos != len(path) - 1:
        paths.append(path[current_slash_pos + 1 :])

    new_paths = []

    for (index, dir) in enumerate(paths):
        if dir == "." or dir == " " or dir == "":
            continue

        if dir == "..":
            new_paths.pop()
            continue

        new_paths.append(dir)

    print(new_paths)
    print("/".join(new_paths))


parser(
    "/home/pragyan/../../etc/../home/pragyan/Python/../JavaScript/./resume-builder/./src/../node_modules"
)
