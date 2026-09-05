Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
b = 98.9
int(b)
98
complex9b)
SyntaxError: unmatched ')'
complex(b)
(98.9+0j)
str(b)
'98.9'
bool(b)
True
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
s = "Anjana"
int(s)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'Anjana'
float(s)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'Anjana'
bool(s)
True
complex(s)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
tuple(s)
('A', 'n', 'j', 'a', 'n', 'a')
set(s)
{'j', 'A', 'n', 'a'}
list(s)
['A', 'n', 'j', 'a', 'n', 'a']
c = 2+5j
int(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
bool(c)
True
set(c)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
list(c)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
str(c)
'(2+5j)'
l = (9,8,6,"hello",3)
int(l)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(l)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'tuple'
bool(l)
True
dict(l)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
str(l)
"(9, 8, 6, 'hello', 3)"
list(l)
[9, 8, 6, 'hello', 3]
tuple(l)
(9, 8, 6, 'hello', 3)
set(l)
{3, 6, 8, 9, 'hello'}
t = ("apple",2,4,6,8)
int(t)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
bool(t)
True
dict(t)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dict(t)
ValueError: dictionary update sequence element #0 has length 5; 2 is required
set(t)
{2, 4, 6, 8, 'apple'}
list(t)
['apple', 2, 4, 6, 8]
str(t)
"('apple', 2, 4, 6, 8)"
s = (set)
s = {"hai","welcome","to","codegnan",63}
int(s)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
bool(s)
True
str(s)
"{'welcome', 'hai', 'codegnan', 'to', 63}"
dict(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 7; 2 is required
list(s)
['welcome', 'hai', 'codegnan', 'to', 63]
tuple(s)
('welcome', 'hai', 'codegnan', 'to', 63)
d =
SyntaxError: invalid syntax
d = {"Name":"Anjana","Batch":63,"Course":"PFS"}
int(d)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(d)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    complex(d)
TypeError: complex() first argument must be a string or a number, not 'dict'
bool(d)
True
str(d)
"{'Name': 'Anjana', 'Batch': 63, 'Course': 'PFS'}"
list(d)
['Name', 'Batch', 'Course']
set)d)
SyntaxError: unmatched ')'
set(d)
{'Course', 'Name', 'Batch'}
tuple(d)
('Name', 'Batch', 'Course')
>>> a = "true"
>>> int(a)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    int(a)
ValueError: invalid literal for int() with base 10: 'true'
>>> a = true
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a = true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a = True
>>> int(a)
1
>>> float(a)
1.0
>>> complex(a)
(1+0j)
>>> str(a)
'True'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    list(a)
TypeError: 'bool' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    dict(a)
TypeError: 'bool' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    tuple(a)
TypeError: 'bool' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    set(a)
TypeError: 'bool' object is not iterable
