from dataclasses import dataclass

@dataclass
class user:
    name: str = 'Aleksey'
    lastname: str = 'Malachow'
    age: int = 21
    email: str = 'aleksey@gmail.com'
    password: str = 213124

    @staticmethod
    def is_adolt(age):
        return age > 18

    @classmethod
    def always_young(cls):
        cls.age = 18
        return cls.age


user1 = user()

print(user1.age)

print(user.is_adolt(21))

print(user.always_young())