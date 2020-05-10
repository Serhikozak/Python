first_digit = int(input('Input first digit '))
second_digit = int(input('Input second digit '))


def compare_digit(b, c):
    a = 5
    d = b + c
    f = b - c

    if c == b:
        return True
    elif d == a:
        return True
    elif f == a:
        return True
    else:
        return 'Enter suitable values'


compare_digit(first_digit, second_digit)
print(compare_digit(first_digit, second_digit))
