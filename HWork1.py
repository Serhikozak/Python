import random

my_list = []

# Create sequence and put it in the list
for i in range(100):
    a = i + 1
    my_list.append(a)
    
random_number = random.choice(my_list)

print(random_number)

Counter_of_try = 0
input_number = 0
while Counter_of_try < 4:
    input_number = int(input('Enter number '))

    if random_number == input_number:
        print('You win')
        break
    elif random_number < input_number:
        print('Enter a lower number')
        break
    elif random_number > input_number:
        print('Enter larger number')
        break


