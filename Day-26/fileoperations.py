#read opration

file=open('pfs-63.txt','r')
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()
'''
'''
with open('pfs-63.txt','r') as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
'''
#write operation
'''
with open('pfs-63.txt','w') as file:
    file.write("Shifted to branch-1")
    '''
#append operation 
'''       
with open('pfs-63.txt','a') as file:
    file.write("Only for today") 
'''
'''
with open('pfs-63.txt','a+') as file:
    file.write("Tomarrow same branch 5")
    file.seek()       
    print(file.read())
'''    
'''
with open('pfs-63.txt','r+') as file:
    file.write("Tomarrow same branch 5")       
    file.seek(0)
    print(file.read()) 
'''       
'''
with open('pfs-63.txt','w+') as file:
    file.write("Tomarrow same branch 5")       
    file.seek(0)
    print(file.read())
'''    