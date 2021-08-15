# Time = O(n) | space = O(n)
def singleCycleCheck(array) -> bool:
    visited_indices = set()
    index = 0

    while True:
        if index in visited_indices:
            break

        element = array[index]

        if index < 0:
            visited_indices.add(len(array) - abs(index))

        else:
            visited_indices.add(index)

        index += element

    return len(visited_indices) == len(array)


def singleCycleCheckBetter(array) -> bool:
    visited_indices = 0
    index = 0

    while True:
        if visited_indices > len(array):
            break

        element = array[index]

        index += element
        visited_indices += 1

    return visited_indices == len(array)


print(singleCycleCheckBetter([2, 3, 1, -4, -4, 2]))
