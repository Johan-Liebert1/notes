"""
given - /foo/../test/../test/../foo//bar/./baz
.. -> went up a dir 
. -> in the same dir

op -> /foo/bar/baz
"""


def parser(path: str) -> "list[str]":
    new_paths = []

    for (index, dir) in enumerate(path.split("/")):
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
