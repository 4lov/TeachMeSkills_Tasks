def calculator(a, b, operation, result):
    if operation == '+':
        result = a + b
        print(result)
        
    
    elif operation == '-':
        result = a - b
        print(result)
    
    elif operation == '*':
        result = a * b
        print(result) 

    elif operation == '/':
        result = a / b
        print(result)

if __name__ == '__main__':
        a = int(input('Введите число '))
        b = int(input('Введите число '))
        operation = input('Введите знак +, -, *,  /,  ')
        result = 0
        calculator(a, b, operation, result)
