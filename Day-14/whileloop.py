
'''i=1
while i<=10:
    print(i)
    i+=1
'''
'''
i=10 
while i>0:
    print(i)
    i-=1
'''
'''
i=2
while i<=100:
    print(i,end=' ') 
    i+=2 
'''
'''
s='Codegnan'

i=len(s)-1
while i>=0:
    print(s[i],end='')
    i-=1
'''
'''
l=[1,0,0,0,2,3,4,5,6,9,12,56,0,4,0,0,16,0]
while 0 in l:
    l.remove(0)
print(l) 
'''
'''
d={}
total_bill=0
while True:
    prod_name=input("Enter the productname (for exit): ")
    if prod_name=='Exit':
        break
    price=int(input("enter the price: "))
    total_bill+=price
    d[prod_name]=price
print (d)
print("Total Bill",total_bill) 
'''
'''
i=0
while i<=10:
    i+=1
    if i==15:
        print(i)
        break
else:
    print("End of the loop") 
'''              
#8,9,11,14,17,18,20
