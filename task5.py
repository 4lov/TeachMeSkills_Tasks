#x = lambda a, b: a ** b
#print(x(2, 5))

#def plus_odin(a):
#    return a + 1
#print (plus_odin(5))

#test = list(map(lambda x: x + 5, {5,6,7}))
#print(test)

#mixed = ['apple', 'grape', 'banana',]
#apples = {}
#def check_is_fruit(fruit: str) -> bool:
#    if fruit == 'apple':
#        return fruit
#test = list(filter(check_is_fruit, mixed))
#print(test)

#filter работает только с bool
#test = [1,2,3,4,5,6,7,8]
#def check_is_odd(number: int) -> bool:
#    return number % 2 ==0

#odd_numbers = list(filter(check_is_odd, test))
#print(odd_numbers)

#from functools import reduce
#numbers = [0,1,2,3,4,5,6,7,8]
#test_reduce = reduce(lambda a, b: a+b ,numbers)
#print(test_reduce)