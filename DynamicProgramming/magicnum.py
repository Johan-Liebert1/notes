def magicNumber(n: int) -> int:
    num = 0

    while True:
        while n > 0:
            num += n % 10
            n = n // 10

        if num < 10:
            return num

        n = num
        num = 0


print(magicNumber(56))
