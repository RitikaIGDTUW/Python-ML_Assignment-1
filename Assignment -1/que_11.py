term=int(input("enter how many terms"))
n1=0
n2=1
count=0
if term<=0:
    print("enter a positive number")
elif(term==1):
     print(n1)   
else:
   print("Fibonacci sequence:")
   while count < term:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1     