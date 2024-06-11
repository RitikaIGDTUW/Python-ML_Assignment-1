from datetime import datetime
birth=int(input("enter your birth year"))
current=datetime.now().year
age=current-birth
print("your age is",age,"years")