from datetime import date, datetime

var = 1
while var == 1:  # This constructs an infinite loop
    any_value = (input('Enter any value '))
    # print("You entered: ", num)
    current_date = date.today()
    current_time = datetime.now().time()
    with open("L5Task5.txt", "a") as file:
        file.write(f'\n{current_date} {current_time} : {any_value}')


