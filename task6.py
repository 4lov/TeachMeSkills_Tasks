#task1
import json
import csv

database = []

name = input('Введите свое имя: ')
age= int(input('Введите свой возраст: '))

data = {
    'name': name,
    'age': age,
    }
json_string = json.dumps(data)
with open('task6.json', 'w') as database:
     database.write(json_string)

with open('task6.csv', 'w') as database:
    names =['Name', 'Age'] 
    file_writer = csv.DictWriter(database, fieldnames = names)
    file_writer.writeheader()
    file_writer.writerow({'Name': name, 'Age': age})
    
#task2
with open('task6.txt', 'w+') as users_file:
    login = input('Логин: ' )
    password = input('Пароль: ')

    credentials = '{}:{}\n'.format(login, password)


    users_file.writelines(credentials)