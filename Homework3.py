while True:
    name = input('Введите ваше имя: ')
    years = int(input('Введите ваш возрас: '))
    if years >= 18:
        print(f'Welcome with club {name}')
    else:
        print(f'Try next time {name}')