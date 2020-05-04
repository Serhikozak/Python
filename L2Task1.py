zero = 0
random_number = int(input('Please input random number'))

if random_number < zero:
    print('You input negative number ', random_number)
elif random_number == zero:
    print('You input zero')
else:
    print('You input positive number ', random_number)

