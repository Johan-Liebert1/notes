def put_underscores(string, array):
    i = 0
    for el in array:
        s, e = el

        string = string[: s + i] + "_" + string[s + i :]
        string = string[: e + 1 + i] + "_" + string[e + 1 + i :]

        i += 2

    return string


def collapse_array(string, array):
    # print(array)
    new_array = []
    new_array_index = 0

    for index, element in enumerate(array):
        if index == 0:
            new_array.append(element)
            new_array_index += 1
            continue

        pe = array[index - 1]

        # [[1, 5], [4, 6]]

        if pe[1] >= element[0]:
            # print(index, new_array_index, new_array)
            new_array[new_array_index - 1][1] = element[1]

        else:
            new_array.append(element)
            new_array_index += 1

    return put_underscores(string, new_array)


def make_array(string, substring):
    i = 0
    array = []

    while i < len(string) - len(substring) + 1:
        index = string[i:].find(substring)

        if index == -1:
            break

        array.append([index + i, index + len(substring) + i])

        i += index + 1

    return collapse_array(string, array)


print(make_array("testthis is a testtest to see if testestest it works", "test"))
