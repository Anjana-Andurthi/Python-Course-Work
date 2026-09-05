Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s=set()
s={1,2,3,4,12,324,9876,34,12431324}
s
{1, 2, 3, 4, 34, 324, 12, 9876, 12431324}
s=set()
l={10,20,30}
m={1,2,3,4}
l+m
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    l+m
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a={1,2,3,4,5}
b={3,5,7,9}
a
{1, 2, 3, 4, 5}
b
{9, 3, 5, 7}
a|b
{1, 2, 3, 4, 5, 7, 9}
a^b
{1, 2, 4, 7, 9}
a&b
{3, 5}
a-b
{1, 2, 4}
a issuperset b
SyntaxError: invalid syntax
a>=b
False
{1}<=b
False
{1}<=a
True
{1,2,3,4}<=a
True
a
{1, 2, 3, 4, 5}
{1,2,3,4,5}<=a
True
b
{9, 3, 5, 7}
a.isdisjoint(b)
False
a.isdisjoint({9,10})
True
a.union(b)
{1, 2, 3, 4, 5, 7, 9}
a.intersection(b)
{3, 5}
a.issubset(b)
False
a.issuperset(b)
False
a
{1, 2, 3, 4, 5}
5 in a
True
b
{9, 3, 5, 7}
2 not in b
True
max(a)
5
min(a)
1
sorted(a)
[1, 2, 3, 4, 5]
sum(a)
15
a
{1, 2, 3, 4, 5}
b=a
b
{1, 2, 3, 4, 5}
b.add(12)
b
{1, 2, 3, 4, 5, 12}
a
{1, 2, 3, 4, 5, 12}
c=a.copy(12)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    c=a.copy(12)
TypeError: set.copy() takes no arguments (1 given)
c=a.copy()
c.add(13)
c
{1, 2, 3, 4, 5, 12, 13}
a
{1, 2, 3, 4, 5, 12}
a.add(123)
a
{1, 2, 3, 4, 5, 123, 12}
a.update({16,17,18})
a
{1, 2, 3, 4, 5, 12, 16, 17, 18, 123}
a.pop()
1
a.pop()
2
a
{3, 4, 5, 12, 16, 17, 18, 123}
a.pop()
3
a.rremove(16)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a.rremove(16)
AttributeError: 'set' object has no attribute 'rremove'. Did you mean: 'remove'?
a.remove(16)
a
{4, 5, 12, 17, 18, 123}
a.remove(12)
a
{4, 5, 17, 18, 123}
a.discard(5)
a
{4, 17, 18, 123}
a.clear()
a
set()
len(a)
0
a
set()
a
set()
a=frozenset({1,12,13,10,18,59,20})
a
frozenset({1, 18, 20, 10, 59, 12, 13})
a.add(12)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a.add(12)
AttributeError: 'frozenset' object has no attribute 'add'
d={}
d=dict()
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2','k3':'v4'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v4'}
d={'k1':'v1','k2':'v2','k3':'v3'}

d={'k1':'v1','k2':'v2','k3':'v3'}
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
id(d)
2618611975808
d['k4']='v4'
d
{'k1': 'v1', 'k2': 'v2', 'k3': 'v3', 'k4': 'v4'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.3]='flt'
d
{1: 'int', 12.3: 'flt'}
d[2+5j]='complex'
d
{1: 'int', 12.3: 'flt', (2+5j): 'complex'}
d['string']='str'
d
{1: 'int', 12.3: 'flt', (2+5j): 'complex', 'string': 'str'}
d[[1,2,3]]='lst'
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    d[[1,2,3]]='lst'
TypeError: unhashable type: 'list'
d[(1,2,3,4)]='tuple'
d
{1: 'int', 12.3: 'flt', (2+5j): 'complex', 'string': 'str', (1, 2, 3, 4): 'tuple'}
d['False']='bool'
d
{1: 'int', 12.3: 'flt', (2+5j): 'complex', 'string': 'str', (1, 2, 3, 4): 'tuple', 'False': 'bool'}
d=
SyntaxError: invalid syntax
d={}
d[1]=1
d[2]
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    d[2]
KeyError: 2
d={}
d[1]=1
d[2]=12.3
>>> d[3]=2+5j
>>> d[4]='str'
>>> d[5]=[1,2,3,4]
>>> d[6]=(1,2,3)
>>> d[7]={1,2,3}
>>> d[8]={1:1}
>>> d[9]=True
>>> d
{1: 1, 2: 12.3, 3: (2+5j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> 9 in d
True
>>> 10 in d
False
>>> str in d
False
>>> d[5]
[1, 2, 3, 4]
>>> d[8]
{1: 1}
>>> d.get(10)
>>> d.get(1)
1
>>> d.get(10,"key is not present")
'key is not present'
>>> d.get(6,"key is not present")
(1, 2, 3)
>>> d
{1: 1, 2: 12.3, 3: (2+5j), 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[3]=4
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: [1, 2, 3, 4], 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[5]=10
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: (1, 2, 3), 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[6]=12
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: 12, 7: {1, 2, 3}, 8: {1: 1}, 9: True}
>>> d[7]=20
>>> d
{1: 1, 2: 12.3, 3: 4, 4: 'str', 5: 10, 6: 12, 7: 20, 8: {1: 1}, 9: True}
