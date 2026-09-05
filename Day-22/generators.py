#generators --> uses yield keyword instead of return by using yield keyword it pause the function
#-->it is a function that produces one value at a time
#-->saves memory and uses for large datasets, when we use yield we also use next() 
'''
def retrivedata():
    data=['1..100','101..200','201..300','301..400','410..500']
    for i in data:
        yield i
reels=retrivedata()
while True:
    status=input("[s]croll or [q]uite: ")
    if status=='s':
        print(next(reels))
    else:
        break
'''
#even number
'''
def even():
    i=0
    while True:
        i+=2
        yield i
n=10
res = even()
for i in range(n):
    print(next(res))
'''
#factors of numbers
'''
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            yield i  
n=12
res = factors(n)
for i in res:
    print(i) 
'''
#prime numbers
'''
def isprime(n):
    for j in range(2,n//2+1):
        if n%j==0:
            return False
    return True
def primes(n):
    for i in range(2,n+1):
        if isprime(i):
            yield i            
n=30
res=primes(n)
for i in res:
    print(i)
'''
#reverse count
'''
def num(n):
    for i in range(n,0,-1):
        yield i                                                  
n=20
res=num(n)
for i in res:
    print(i)
'''    