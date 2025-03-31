'''
Find two closest number in two arrays
'''


def smallestDifference(array1, array2):
    array1 = sorted(array1)
    array2 = sorted(array2)

    i, j = 0, 0

    smallestDiff = float('inf')
    elements = []

    while i < len(array1) and j < len(array2):
        if array1[i] == array2[j]:
            if abs(array1[i] - array2[j]) < smallestDiff:
                smallestDiff = abs(array1[i] - array2[j])
                elements = [array1[i], array2[j]]

            i += 1
            j += 1

        elif array1[i] < array2[j]:
            if abs(array1[i] - array2[j]) < smallestDiff:
                elements = [array1[i], array2[j]]
                smallestDiff = abs(array1[i] - array2[j])

            i += 1

        elif array1[i] > array2[j]:
            if abs(array1[i] - array2[j]) < smallestDiff:
                elements = [array1[i], array2[j]]
                smallestDiff = abs(array1[i] - array2[j])

            j += 1

    return elements, smallestDiff


a = [-1, 5, 10, 20, 28, 3]
b = [26, 134, 135, 15, 17]

print(smallestDifference(a, b))
