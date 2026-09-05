Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
c='python programming'
len(c)
18
ord('p')
112
ord('a'\)
    
SyntaxError: unexpected character after line continuation character
ord('0')
    
48
ord('A')
    
65
chr(65)
    
'A'
chr(66)
    
'B'
min(c)
    
' '
max(c)
    
'y'
sorted(c)
    
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
c='String is immutable'
    
c
    
'String is immutable'
c.upper()
    
'STRING IS IMMUTABLE'
c.lower()
    
'string is immutable'
c.capitalized()
    
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    c.capitalized()
AttributeError: 'str' object has no attribute 'capitalized'. Did you mean: 'capitalize'?
c.capitalize()
    
'String is immutable'
c.title()
    
'String Is Immutable'
c.swap()
    
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    c.swap()
AttributeError: 'str' object has no attribute 'swap'
c.swapcase()
    
'sTRING IS IMMUTABLE'
c
    
'String is immutable'
c.center(60,'0')
    
'00000000000000000000String is immutable000000000000000000000'
c.ljust(60,'_')
    
'String is immutable_________________________________________'
c.rjust(60,'-')
    
'-----------------------------------------String is immutable'
c.center(60,'-')
    
'--------------------String is immutable---------------------'
'12'.zfill(4)
    
'0012'
c.find('i')
    
3
c.find('z')
    
-1
c.rfind('i'0
        
SyntaxError: '(' was never closed

c.rfind('i')
        
10
c
        
'String is immutable'
c.index('i')
        
3
c.rindex('z')
        
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    c.rindex('z')
ValueError: substring not found
c.index('s'0
        
SyntaxError: '(' was never closed
c.index('s')
        
8
c.count('g')
        
1
c.count('m')
        
2
c.replace('i','o')
        
'Strong os ommutable'
c.replace('String','Float')
        
'Float is immutable'
c.translate(c.maketrans('aeiou','12345'))
        
'Str3ng 3s 3mm5t1bl2'
c.maketrans('aeiou','12345')
        
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
        
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
c.split()
        
['String', 'is', 'immutable']
'string,is,immutable'.split()
        
['string,is,immutable']
'string,is,immutable'.split(',')
        
['string', 'is', 'immutable']
'string,is,immutable'.rsplit()
        
['string,is,immutable']
'string,is,immutable'.split(',',1)
        
['string', 'is,immutable']
'''
python
programming
lang'''
        
'\npython\nprogramming\nlang'
s.splitlines()
        
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    s.splitlines()
NameError: name 's' is not defined
s
        
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    s
NameError: name 's' is not defined
s='''
python
programming
lang'''
        
s
        
'\npython\nprogramming\nlang'
s.splitlines()
        
['', 'python', 'programming', 'lang']

['', 'python', 'programming', 'lang'].join()
        
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    ['', 'python', 'programming', 'lang'].join()
AttributeError: 'list' object has no attribute 'join'
''.join(['','python', 'programming', 'lang'])
        
'pythonprogramminglang'
'-'.join(['','python', 'programming', 'lang'])
        
'-python-programming-lang'
'python.py'.partition('.')
        
('python', '.', 'py')
s='java','python','c','c++'
        
s.partition('.')
...         
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    s.partition('.')
AttributeError: 'tuple' object has no attribute 'partition'
>>> s.partition(',')
...         
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    s.partition(',')
AttributeError: 'tuple' object has no attribute 'partition'
>>> s="java,python,c,c++"
...         
>>> s.partition(',')
...         
('java', ',', 'python,c,c++')
>>> s.rpartition(',')
...         
('java,python,c', ',', 'c++')
>>> c='   hello     world     '
...         
>>> c.strip()
...         
'hello     world'
>>> c.lstrip()
...         
'hello     world     '
>>> c.rstrip()
...         
'   hello     world'
>>> text="Hello 🙂"
...         
>>> text.encode()
...         
b'Hello \xf0\x9f\x99\x82'
>>> 
>>> b'Hello \xf0\x9f\x99\x82'.decode()
...         
'Hello 🙂'
