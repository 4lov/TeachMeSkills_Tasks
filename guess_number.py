import random
tries = 0
number = random.randint(1, 50)
while tries < 6:
    guess = int(input('try to guess number between 1 and 50: '))
    tries += 1
    if guess < number:
        print('too low')
    if guess > number:
        print('too high')
    if guess == number:
        print('exactly, congratulacion')
        break
    if guess != number and tries == 6:
        print(f'Sorry, but my number was: {number}, try again')
        break