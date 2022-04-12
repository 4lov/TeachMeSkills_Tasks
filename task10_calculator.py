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
        a = float(input('Введите число '))
        b = float(input('Введите число '))
        operation = input('Введите знак +, -, *,  /,  ')
        result = 0
        calculator(a, b, operation, result)
