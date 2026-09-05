
'''#lambda function: it is a small function without using the def keyword

#greater
greater = lambda a,b: a if a>b else b
print(greater(12,13))
print(greater(50,83))
print(greater(40,20))
print(greater(16,26))

#welcome
wish=lambda name:f'Welcome to the course {name}'
print(wish("Anjana"))
print(wish("Manothra"))
print(wish("Amani"))

#even or odd

iseven = lambda n:"Even" if n%2==0 else "Odd"
print(iseven(45))
print(iseven(18))
print(iseven(76))

#avg

avg=lambda a,b,c : (a+b+c)/3
print(avg(4,5,6))
print(avg(9,8,7))
'''
#calculate domain
'''
domain=lambda mail:(mail.split('@')[-1]).split('.')[0]

print(domain('Anjana@codegan.com'))
print(domain('Anjana@gmail.com'))
print(domain('Anjana@outlook.com'))
print(domain('Anjana@Yahooo.com'))
'''
'''
#calculate gst
gst=lambda price:price+price*0.18
print(gst(1000))
print(gst(8000))
print(gst(3000))
print(gst(5000))
'''
'''
#map with lambda
#Price list
prices=[5433,8798,6778,3456,9766,1234]  
res=list(map(lambda price:price+price*0.18,prices))
print(res)
'''
'''
#list of names
names=['anjana','amani','sri','manothra','bhuvi']
res=list(map(lambda name:name.title(),names))
print(res)
'''
'''
#list of prices with 30% dis
prices=[2343,9876,4567,3857,8374,8765]
res=(list(map(lambda price:price-price*0.3,prices)))
print(res)
'''
'''
#filter with lambda 
prices=[2345,9876,5647,8473,6473,4324,8490]
res=(list(filter(lambda price:price>5000,prices)))
print(res)
'''
'''
prices=[2345,9876,5647,8473,6473,4324,8490]
res=(list(filter(lambda price:price%2!=0,prices)))
print(res)
'''
'''
names={'anjana','amani','sri','manothra','bhuvi'}
res=list(filter(lambda name:len(name)>5,names))
print(res)
'''
'''
from functools import reduce
l=[3,567,6,24,124,87,789]
res=reduce(lambda sum,i:sum+i,l)
print(res)

names=['anjana','amani','sri','manothra','bhuvi']
res=reduce(lambda res, i:res + ' '+i, names)
print(res)
'''
#sorted with lambda
products={'Sugar':40,
          'Salt':20,
          'Eggs':30,
          'Bread':45,
          'Cooking Oil':120
        }
print(dict(sorted(products.items())))
print(dict(sorted(products.items(),reverse=True)))
print(dict(sorted(products.items(),key=lambda i:i[1])))
print(dict(sorted(products.items(),key=lambda i:i[1],reverse=True)))