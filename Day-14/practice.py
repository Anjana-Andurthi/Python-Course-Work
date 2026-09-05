#numbers from 1toN
'''
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(i)
'''
'''
#even numbers from 1 to N
n=int(input("Enter the integer: "))
for i in range(2, n+1 ,2):
    print(i)
'''
#sum of numbers from 1 to N
'''
n=int(input("Enter the Number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum=",sum)
'''
#odd numbers
'''
n=int(input("Enter the number: "))
for i in range(1,n+1,2):
    print(i)
'''
#Factorial
'''
n=int(input("Enter the number: ")) 
fact=1
for i in range(1,n+1):
    fact *=i
print(f"Factorial of {n} is {fact}")
'''
#Multiplication table
'''
n=int(input("Enter the number: ")) 
for i in range(1,11):
    print(f"{n}*{i}={n*i}") 
'''
#prime number
'''
n=int(input("Enter the number: "))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not a prime number")
        break
else:
    print("Prime number")
'''
#count numbers divisible by 3
'''
n=int(input("Enter the number: "))
count=0
for i in range(1,n+1):
    if i %3==0:
        count+=1
print("Count=",count)
'''
#multiples of 5 
'''
n=int(input("Enter the number: "))
for i in range(5,n+1,5):
    print(i,end=" ")
'''
#sum of first N natural numbers
'''
n=int(input("Enter the number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("sum=",sum)
'''
#print numbers from n to 1
'''
n=int(input("Enter the number: "))
i=n 
while i>0:
    print(i)
    i-=1
'''
#divisible by 3 and 5
'''
n=int(input("Enter the number: "))
count = 0
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        count+=1
print("Count=",count)
'''               



