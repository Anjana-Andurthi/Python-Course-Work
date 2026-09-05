'''
def display(n):
    n=n+10
    print('inside:',n)
n=10
display(n)
print('outside:',n) 
'''
'''
def display():
    print('Inside:',n)

n=10
display()
print('Outside:',n)  
'''
'''
def display():
    n=10
    print('Inside:',n)

display()
print('Outside:',n)    
'''
'''
def display():
    global n
    n=n+10
    print('inside:',n)
n=10
display()
print('outside:',n) 
'''
'''
def display():
    global n
    n='PFS'
    print("Updated course:",n)

n='JFS'
display()
print("Final course:",n)
'''
'''
def display():
    n='JFS'
    def update():
        nonlocal n
        n='PFS'    
        print("Updated course",n)
    update()
    print("Final course:",n)

display() 
'''
# whenever builtin functions as variables it act as variable instead of function
l=[1,2,3,4,5]
max=20
sum=10
print(sum)       