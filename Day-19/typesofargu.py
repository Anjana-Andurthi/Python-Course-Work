# Position argu
'''
def display(name,email,password):
    print(f'name : {name}')
    print(f'email : {email}')
    print(f'password : {password}')

display('Xyz','Xyz@gmail.com','Xyz123')
display('Xyz@gmail.com','Xyz123','Xyz')
display('Xyz123','Xyz@gmail.com','Xyz')
'''
#keyword argu
'''
def display(name,email,password):
    print(f'name : {name}')
    print(f'email : {email}')
    print(f'password : {password}')

display(name='Xyz',email='Xyz@gmail.com',password='Xyz123')
display(email='Xyz@gmail.com',password='Xyz123',name='Xyz')
display(password='Xyz123',email='Xyz@gmail.com',name='Xyz')
'''
#default argu
'''
def display(name,email='gmail.com',password=''):
    print(f'name : {name}')
    print(f'email : {email}')
    print(f'password : {password}')

display('Xyz','Xyz@gmail.com','Xyz123')
display('Xyz','Xyz@gmail.com')
display('Xyz')
'''
#variable len argu
'''
def display(*names):
    print(names)

display('Anjana')
display('Anjana','Amani')
display('Anjana','Amani','Sriharsha')
display('Anjana','Amani','Sriharsha','Abhi')
'''
def display(**products):
    print(products)

display(bag=5000)
display(bag=5000,book=20)
display(bag=5000,book=20,bottle=300)



