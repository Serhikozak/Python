import random

random_number = random.randint(1, 100)
# print(random_number)
Counter_of_try = 0
input_number = 0
print('Enter number, you have 4 attempts ')
while Counter_of_try <= 4:
    Counter_of_try = Counter_of_try + 1
    input_number = int(input())

    if random_number == input_number:
        print('You win')
        break
    elif random_number < input_number:
        print('Enter a lower number ')

    elif random_number > input_number:
        print('Enter larger number ')

    if Counter_of_try == 4:
        print("We used all the attempts")



