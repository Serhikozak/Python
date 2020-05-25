from datetime import date, datetime


def deco(func):
    def wrapper(a, b):
        print('Hello ', end='')
        result = func(a, b)
        print('Goodbye')
        return result

    return wrapper


@deco
def start(a, b):
    c = a + b
    print(c, end=' ')


target_result = start(20, 60)


current_date = date.today()
current_time = datetime.now().time()
with open("logs.txt", "a") as file:
    file.write(f'\n{current_date} {current_time} : {result}')
