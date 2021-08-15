# Product Of Array Except Self

def prod(arr):
    new_arr = [1] * len(arr)
    for i in range(len(arr)):
        prod = 1
        for j in range(len(arr)):
            if i != j:
                prod *= arr[j]

        new_arr[i] = prod
    return new_arr


def better_prod(arr):
    max_prod = 1
    for i in arr:
        if i != 0:
            max_prod *= i

        
    for i in range(len(arr)):
        arr[i] = max_prod // arr[i]

    return arr


# solving without divsion

def better_prod_without_division(arr):
    left_array_prod = [1] * len(arr)
    right_array_prod = [1] * len(arr)
    total_prod = []
    left_prod = 1
    right_prod = 1

    for i in range(1, len(arr)):
        left_prod *= arr[i - 1]
        left_array_prod[i] = left_prod

    for j in range(len(arr) - 2, -1, -1):
        right_prod *= arr[j + 1]
        right_array_prod[j] = right_prod

    # print(left_array_prod)
    # print(right_array_prod)

    for k in range(len(arr)):
        total_prod.append(left_array_prod[k] * right_array_prod[k])

    return total_prod


print(better_prod_without_division([1,2,3,4]))