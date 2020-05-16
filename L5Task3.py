import random
import time

beginning = time.time()
my_list = [random.randint(0, 100000) for i in range(0, 1000)]
end_operation = time.time()
print(end_operation - beginning)
