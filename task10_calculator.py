def calculator(a, b, operation):
  
    if operation == '+':
      return a + b
        
    
    elif operation == '-':
        return a - b
        
    
    elif operation == '*':
        return a * b
        
    elif operation == '/':
        return a / b

while True: 
    try:          
        a = float(input('Введите число '))
        break
    except ValueError:
        print('Ты не ввел число')
while True:   
        operation = input('Введите знак +, -, *,  /,  ')
        if operation in ['+', '-', '*', '/']:
            break
        print('Не правильный оператор')
while True:
    try:          
        b = float(input('Введите число '))
        break
    except ValueError:
        print('Ты не ввел число')
try: 
    print(calculator(a, b ,operation))
except ZeroDivisionError:
    print('На 0 делить нельзя')


    