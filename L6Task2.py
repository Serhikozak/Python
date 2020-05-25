# Passwords generator
import string
import random


# One way generate password
# chars = string.digits + string.ascii_letters + string.punctuation

# pass_list = [random.choice(chars) for i in range(12)]
# # print(pass_list)
# password = str(''.join(pass_list))
# print(password)

# with open("Pass.txt", "a") as file:
#     file.write(f'\n{password}')


def password() -> object:  # Two way generate password
    chars = string.digits + string.ascii_letters + string.punctuation
    return str(''.join([random.choice(chars) for i in range(12)]))


ps = password()
print(ps)

with open("Pass.txt", "a") as file:
    file.write(f'\n{ps}')


# def password() -> list:
#     chars = string.digits + string.ascii_letters + string.punctuation
#     return chars
#
#
# result = str(map(lambda random.choice(n) for n in range(12), password()))
#
# print(''.join(result))