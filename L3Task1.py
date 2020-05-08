# Create of list random number and define even number
# if that list haven't any even number we get an appropriate print('In that list, not have even number')
import random

n = int(input('Input any number '))
my_list = [random.randint(0, 88) for i in range(n)]
print(my_list)
my_list_even_number = []
for my_list in my_list:
    if my_list % 2 == 0:
        my_list_even_number.append(my_list)

if len(my_list_even_number) > 0:
    print(my_list_even_number)
else:
    print('In that list, not have even number')


