# Determine palindrom
symbols = input('Enter some symbols ')

str_length = len(symbols)

for i in range(str_length // 2):
    if symbols[i] != symbols[-1 - i]:
        print("It's not palindrome")
        quit()

print('It\'s palindrome')
