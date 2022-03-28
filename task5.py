#task1
def show_car_info(engine_info):
    def wrapper():
        print('Зелёный цвет, седан')
        engine_info()
    return wrapper

#task 2
x = lambda a: a ** 2
print(x(int(input('Введите число: '))))

#task3
@show_car_info
def show_engine_info():
    print('v8 3 литра бензин')

show_engine_info()