def cce(string, number):
    # 97 to 122
    new_str = ''
    for i in string:
        if ord(i) + number > 122:
            roll_over_by = (ord(i) + number) - 122
            new_str += chr(97 + roll_over_by - 1)

        else:
            new_str += chr(ord(i) + number)

    return new_str


