def fibonacci(n):
    if n <= 2:
        return 1

    first = 1
    second = 1
    count = 2

    while True:
        third = first + second
        count += 1

        if count == n:
            return third

        first = second
        second = third


# for i in range(1, 11000):
print(f'{11000} : {fibonacci(25)}')
