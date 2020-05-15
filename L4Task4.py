import random
my_list = [random.randint(2, 8) for i in range(1, 9)]
number_inner_list = random.choice(my_list)
quantity_lists = random.choice(my_list)
new_list = []

print(quantity_lists)
print(number_inner_list)


data = [[random.randint(1, 10) for i in range(0, number_inner_list)] for j in range(0, quantity_lists)]
print(data)
print(sum(data, []))
new_list.append(sum(sum(data, [])))
print(new_list)

