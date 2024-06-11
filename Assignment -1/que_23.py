a=int(input("enter the temperature"))
print("choice 1 : to convert degree into fahrenheit")
print("choice 2 : to convert fahrenheit into degree")
b=int(input("enter choice"))
if b==1:
    c=(a * 9/5) + 32
    print("in fahrenheit: ", c,"F")
else:
    d= (a - 32) * 5/9   
    print("in celcius", d,"C")