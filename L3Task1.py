# Create of list random number and define even number
import random

n = int(input('Input any number '))
my_list = [random.randint(0, 88) for i in range(n)]
print(my_list)
for my_list in my_list:
    if my_list % 2 == 0:
        print(my_list)
    elif my_list % 2 == 1:
        print('In that list, not have even number')
    # else:
    #     my_list % 2 == 1
    # print('In that list, not have even number')
