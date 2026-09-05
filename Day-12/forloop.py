#str list tuple set dict range()
'''
for var in seq:
    print(var)
'''
'''
s='Codegnan'
for ch in s:
    if ch in 'aeiouAEIOU':
        print(ch)'''
'''
l=[10,23,30,45,1,3,4,8,7]
for i in l:
    if i%2==0:
        print(i,"Even")
    else:
        print(i,"Odd")    '''

'''marks=(90,20,35,46,78,89,10,48)          
for mark in marks:
    if mark>35:
        print(mark,"Pass") 
    else:
        print(mark,"Fail")     '''
'''
followers={'Anjana','Amani','Sriharsha','Abhi'}  
for i in followers:
    print(i) 
    '''
'''    
bus={'s1':'Booked','s2':'Available','s3':'Available','s4':'Booked','s5':'Available'}  
for seat in bus:
    if bus.get(seat)=='Available':
        print(seat,bus.get(seat))
'''
#range(start,end+1,step)=(0,nodef,1)  
'''
for i in range(1,11):
    print(i)
'''
'''
for i in range(2,51,2):
    print(i)'''
'''
for i in range(1,100,2):
    print(i,end=' ') 
'''
'''
for i in range(5,51,5):
    print(i)  
'''
n=int(input("Enter the table:")) 
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")        