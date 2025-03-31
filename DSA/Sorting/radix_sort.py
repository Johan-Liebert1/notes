def radix_sort(array: list[int]):
    if len(array) == 0:
        return array

    maxx = max(array)

    passes = len(str(maxx))

    for pass_ in range(passes):
        bins = [[] for _ in range(10)]

        for i in array:
            bin_idx = (i // 10 ** pass_) % 10
            bins[bin_idx].append(i)

        idx = 0

        for b in bins:
            for e in b:
                array[idx] = e
                idx += 1

    return array


from helpers import get_test_case

for case in get_test_case(20, True):
    print(sorted(case[:]) == radix_sort(case))
