from dataclasses import dataclass
import random

@dataclass
class user:
    name: str
    lastname: str
    age: int
    email: str
    password: str

    @staticmethod
    def is_adolt(age):
        return age > 18

    @classmethod
    def always_young(cls, age):
        return cls(18)

user1 = user('Aleksey', 'Malachow', 21, 'aleksey@gmail.com', 213214)

print(user1.age)

print(user.is_adolt(21))

#print(user.always_young())