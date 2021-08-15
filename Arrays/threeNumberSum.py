def three_number_sum(array, target):
    p2 = 0
    p3 = len(array) - 1

    values = []

    array = sorted(array)

    for p1 in range(len(array) - 2):
        p2 = p1 + 1
        p3 = len(array) - 1

        while p3 > p2:
            summ = array[p1] + array[p2] + array[p3]

            if summ == target:
                values.append([array[p1], array[p2], array[p3]])
                p2 += 1
                p3 -= 1

            elif summ < target:
                p2 += 1

            elif summ > target:
                p3 -= 1

    return values


print(three_number_sum([-8, -6, 1, 2, 3, 5, 6, 12], 0))
