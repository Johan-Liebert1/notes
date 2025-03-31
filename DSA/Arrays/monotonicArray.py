def monotonicArray1(array):
    inc = False

    # check what direction the array is going (increasing or decreasing)
    for i in range(1, len(array)):
        if array[i - 1] < array[i]: 
            inc = True
            break

        elif array[i - 1] > array[i]:
            inc = False
            break
    
    if i == len(array) - 1: return True

    for j in range(i, len(array)):
        if inc and array[j - 1] > array[j]:
            return False

        elif not inc and array[j - 1] < array[j]:
            return False

    return True

print(monotonicArray1())
