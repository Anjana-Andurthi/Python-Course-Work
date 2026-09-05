#int float str list tuple set dict bool

#int float str tuple bool -immutable-doesnot effect the outside 
#list set dict-mutable-it act as passbyreference -it effect the outside
#dict
'''
def display(n):
    n[5]=6
    print("Inside:",n)

n={1:2,3:4}
display(n)
print('Outside:',n)
'''
#int
'''
def display(n):
    n+=6
    print("Inside:",n)

n=10
display(n)
print('Outside:',n)
'''
#float
'''
def display(n):
    n+=10.6
    print("Inside:",n)

n=10.6
display(n)
print('Outside:',n)
'''
#string
'''
def display(n):
    n+="lang"
    print("Inside:",n)

n="Python"
display(n)
print('Outside:',n)
'''
#bool
'''
def display(n):
    n=True
    print("Inside:",n)

n=False
display(n)
print('Outside:',n)
'''
#set
'''
def display(n):
    n.add(5)
    print("Inside:",n)

n={1,2,3,4}
display(n)
print('Outside:',n) 
'''
#tuple
'''
def display(n):
    n=(1,2,3,4)
    print("Inside:",n)

n=(5,6,7)
display(n)
print('Outside:',n) 
'''  