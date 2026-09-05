#from 1-20
'''
res=[i for i in range(5,21)]
print(res)
'''
#squares of numbers
'''
res=[i**2 for i in range(1,11)]
print(res)
'''
#cubes of numbers
'''
res=[i**3 for i in range(1,11)]
print(res)
'''
#even numbers
'''
r=list(map(int,input("Enter the list: ").split()))
res=[i for i in r if i%2==0]
print(res)
'''
#odd numbers
'''
n=list(map(int,input("Enter the list: ").split()))
l=[i for i in n if i%2!=0]
print(l)
'''
#all words into uppercase
'''
n=(input("Enter the list of words: ").split())
uppercase=[word.upper() for word in n]
print(uppercase)
'''
#all words into lowercase
'''
n=(input("Enter the list of words: ").split())
lowercase=[word.lower() for word in n]
print(lowercase)
'''
#greater than 10 from a list
'''
n=list(map(int,input("Enter the list of numbers: ").split()))
l=[i for i in n if i>10]
print(l)
'''
#divisible by 5
'''
n=list(map(int,input("Enter the numbers: ").split()))
l=[i for i in n if i%5==0]
print(l)
'''
#positive numbers from a list
'''
n=[-5,10,-3,7,0]
l=[i for i in n if i>0 ]
print(l)
'''
#negative numbers from a list
'''
n=[-5,10,-3,7,-1]
l=[i for i in n if i<0]
print(l)
'''
#length of word
'''
words=["cat","dog","python"]
l=[len(word) for word in words]
print(l)
'''
#vowels from string
'''
s=(input("Enter the string: "))
l=[char for char in s if char in ('a','e','i','o','u','A','E','I','O','U')]
print(l)
'''