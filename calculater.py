def calculater():
    try:
        num1=float(input('enter first number: '))
        num2=float(input('enter second number: '))
        operation=input('Choose any operation(+,-,*,/): ')

        if operation == '+':
            result=num1+num2
        elif operation == '-':
            result=num1-num2
        elif operation == '*':
            result=num1*num2
        elif operation == '/':
            if num2 != 0:
                result=num1/num2
            else:
                print('Error: Division by zero is not allowed.')
                return
        else:
            print('please enter operation in +,-,* or / .')
            return
        print(f"Result:{result}")
    except ValueError:
         print('Error: please enter any value.')
calculater()         

