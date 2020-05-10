# Sum of random List
import random


def sum_my_list(s):
    return sum(s)


quantity_number = int(input('Input any number '))
my_list = [random.randint(0, 10) for i in range(quantity_number)]
print(my_list)
result = sum_my_list(my_list)
print(result)


