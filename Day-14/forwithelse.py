#when break is exceuted  else will never exceuted
#no break - else part is exceuted
'''
for i in range(1,10):
    if i==15:
        break
    print(i)

else:
    print("End of the Loop")
'''
'''
pin=1234

for _ in range(5):
    epin=int(input("Enter the pin: "))
    if pin==epin:
        print("Unlock Phone")
        break
    else:
        print("Invalid Pin")
else:
    print("Try after 30 seconds.")
'''
#factors of a number
'''
n=int(input("Enter the number: "))
print("Factorial: " ,end=' ')     
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')
'''
#prime number
'''
n=int(input("Enter the number: "))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("Prime Number")
else:
    print("Not a prime number")
'''
'''
n=int(input("Enter the number: "))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("Prime number")
'''
                        

