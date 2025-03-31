def isCryptSolution(crypt, solution):
    mapping = {}
    ints = []

    for row in solution:
        mapping[row[0]] = row[1]

    for word in crypt:
        string_of_numbers = ''
        for i in word:
            string_of_numbers += mapping[i]

        if len(string_of_numbers) > 1 and string_of_numbers[0] == '0':
            return False

        else:
            ints.append(string_of_numbers)

    return int(ints[0]) + int(ints[1]) == int(ints[2])


    