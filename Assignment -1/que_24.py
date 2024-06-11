a=float(input("enter the num1"))
b=float(input("enter the num2"))
c=input("enter an operator (+, -, *, /): ")
if c == '+':
        result = a+b
elif c == '-':
        result = a-b
elif c == '*':
        result = a*b
elif c == '/':
        result = a/b
else:
        result = "Error: Invalid operator!"
print("the result is ",result)