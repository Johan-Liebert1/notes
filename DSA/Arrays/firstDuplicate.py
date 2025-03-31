def firstDuplicate(array):
    dictionary = {}

    for i in range(len(array)):
        if array[i] not in dictionary:
            dictionary[array[i]] = 1

        else:
            dictionary[array[i]] += 1

            if dictionary[array[i]] == 2:
                return array[i]

    return -1

print(firstDuplicate([1,2,3,4,5,6]))
        