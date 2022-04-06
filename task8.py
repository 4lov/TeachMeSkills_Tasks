# создать класс
# сделать класс наследник
# переопределить метод родителя
# перегрузить метод init


class Human:
    def __init__(self, name: str , last_name: str, age: int):
        self.name = name
        self.last_name = last_name
        self.age = age
        
    def run(self, run):
        return run 

class Alien(Human):
    def __init__(self, height: int, **kwargs):
        self.height = height
        self.Friendly = True
        super().__init__(**kwargs)

    def run(self, run):
        return run 

Aliens = Alien(
    name = 'Pol',
    last_name = 'ALien',
    age = 777,
    height = 140
)

print(Aliens.name)
print(Aliens.last_name)
print(Aliens.age)
print(Aliens.height)
