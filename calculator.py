import math

first_number= float(input("enter first number"))
sign= input("enter an operator (+, -, *, /)")
second_number= float(input("enter second number"))

if sign == '+':
    result = first_number + second_number
    print(result)
elif sign == '-' :
    result= first_number - second_number
    print(result)
elif sign == '*':
    result = first_number * second_number
    print(result)
elif sign == '/':
    result = first_number / second_number
    print(result)

else:
    print('invalid operator')



