# file which create copy to new file
import random
import shutil

# Create random quantity of number inner list and quantity of list
my_list = [random.randint(2, 8) for i in range(1, 9)]
number_inner_list = random.choice(my_list)
quantity_lists = random.choice(my_list)
new_list = []

print(quantity_lists)
print(number_inner_list)

# Create random list
data = [[random.randint(1, 10) for i in range(0, number_inner_list)] for j in range(0, quantity_lists)]
print(data)
# Extract all values from all lists into the new list and sum them
print(sum(data, []))
new_list.append(sum(sum(data, [])))
print(new_list)


# Copy existing file to another file which is called script.copy.py
shutil.copy(r'L5Task1.py', r'script.copy.py')
# file.close()



