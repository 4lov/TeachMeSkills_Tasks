#task 1
generator = [i for i in range(1, 20)]
print(generator)
#task 2
def get_numbers_list(amount: list)-> list: 
    return [i for i in range (amount + 1)]
print(get_numbers_list(10))
