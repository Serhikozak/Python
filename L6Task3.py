# Choice of a longest word
input_string = input('enter string: ').split()
print(input_string)
count = 0
for i in input_string:
    if len(i) > count:
        count = len(i)
        word: str = i

print('the longest word is: ', word)

# input_string = input('enter string: ')
# print(max(input_string.split(), key=lambda number_of_letters: len(number_of_letters)))

# str_we = 'bdfbchdjdnmxc djudjdjdj dnjdnd'
# print(str_we.split())