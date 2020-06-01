import json
from datetime import datetime
import os

JSON_FILE_NAME = 'notebook.json'

name = input('Enter your name ')
surname = input('Enter your surname ')

try:
    phone_number = int(input('Enter your phone_number '))
except:
    print('You enter bad data')
    phone_number = 1

address = input('Enter your address ')


current_time = datetime.now().time()
my_notebook = (f'{current_time} : {name} {surname}'
               f' {phone_number} {address}')


file_json = open(JSON_FILE_NAME, 'a')
json.dump(my_notebook, file_json)

print('1.open file')
print('2.Clear file')
my_file = int(input())

if my_file == 1:
    # file_json = open(JSON_FILE_NAME)
    os.open(JSON_FILE_NAME, os.O_RDONLY)
elif my_file == 2:
    os.remove(JSON_FILE_NAME)





