import random
from math import sqrt
from statistics import median


my_list = [4, 9, 25, 36, 49, 64]


# def sqrt_list(a) -> float:
#     return sqrt(a)


# result = list(map(sqrt_list, my_list))
result = list(map(lambda n: sqrt(n), my_list))
print(result)
m_result = median(result)
print(m_result)


end_result = list(filter(lambda x: x > m_result, result))
print(end_result)





