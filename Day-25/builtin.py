#builtin modules: os module-->
#system module-->sys.path,sys.version,sys.exit
#platform--> about the system like windows mac that contains platform.system,,platform.processor
#math module-->all the mathematical things
#random module--> generate a random value in btw the range
'''
import sys

print(sys.path)
print(sys.version)
print("start")
sys.exit()
print("end")platform.release
'''
'''
import platform

print(platform.system())
print(platform.release())
print(platform.processor())
'''
'''
import math
print(math.pi) #pi value
print(math.e)

print(math.sqrt(36))
print(math.pow(2,3)) #power of value

print(math.ceil(12.000001))# gives upper bound
print(math.ceil(12.3))
print(math.ceil(12.6))
print(math.ceil(12.999999))

print(math.floor(12.00001))  #always gives lower bound
print(math.floor(12.3))
print(math.floor(12.6))
print(math.fabs(-10))  #fabs-gives float values,abs-never gives a negative value
print(math.factorial(5))
print(math.gcd(8,24))
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
'''
'''
import random
random.seed(10) # gives always a same values
print(random.randint(1,10))
print(random.randint(10000,999999))#gives in btwm range 
print(random.random())
print(random.uniform(1,6))#gives float values
l=['R','P','S']
print(random.choice(l)) #gives a random choice
print(random.choices(l,k=2))

random.shuffle(l) #shuffles the values in list
print(l)
'''
'''
from collections import Counter,defaultdict
s='python programming'
m='this is that that is this is is'.split()
l=[1,1,1,1,3,2,4,5,45,124,12,34,23,221,67,1,9,4,32]
#print(Counter(s))
#print(Counter(m))
#print(Counter(l))
d=defaultdict(int)
for i in s:
    d[i]+=1

print(d)   
'''
'''
from collections import deque
l=deque([])
l.append(10) 
l.append(20) 
l.append(30) 
l.popleft() 
l.popleft() 
l.append(50) 
l.append(70) 
l.popleft()

print(l)
'''
'''
from collections import deque
l=deque([])
l.appendleft(10) 
l.appendleft(20) 
l.appendleft(30) 
l.pop() 
l.pop() 
l.appendleft(50) 
l.appendleft(70) 
l.pop()

print(l)
'''
from itertools import combinations,permutations
res1=list(combinations('abc',2))
res2=list(permutations('abc',2))
print([''.join(i) for i in res1])
print([''.join(i) for i in res2])

['ab','bc','ca']



