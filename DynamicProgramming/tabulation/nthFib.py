def nthFib(n):
    array = [0] * (n + 1)
    array[1] = 1

    for i in range(0, len(array) - 2):
        array[i + 1] += array[i]
        array[i + 2] += array[i]

    array[-1] += array[-2]

    return array[n]


print(nthFib(60))
