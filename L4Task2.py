s = int(input('Enter four digit number '))
f = str(s)
my_list = []
print(f)
for i in f:
    my_list.append(int(i))
print(sum(my_list))
