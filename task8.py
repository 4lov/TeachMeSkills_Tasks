# создать класс
# сделать класс наследник
# переопределить метод родителя
# перегрузить метод init


class human:
    def __init__(self, name: str , last_name: str, age: int):
        self.name = name
        self.last_name = last_name
        self.age = age


class alien(human):
    def __init__(self, height: int, **kwargs):
        self.height = height
        self.Friendly = True
        super().__init__(**kwargs)


alien = alien(
    name = 'Pol',
    last_name = 'ALien',
    age = 777,
    height = 140
)

print(alien.name)
print(alien.last_name)
print(alien.age)
print(alien.height)
