def gcd_recursive(a, b):
    if a == 0 or b == 0:
        return max(a, b)

    else:
        return gcd_recursive(b, a % b)


def gcd_iterative(a, b):
    if a == 0 or b == 0:
        return max(a, b)

    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return b


print(gcd_iterative(360, 71))
