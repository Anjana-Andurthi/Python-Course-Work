Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[1,2,3,4,5]
l[10,,,7,6,1,2,3,4]
SyntaxError: invalid syntax
l=[10,9,7,6,1,2,3,4]
l
[10, 9, 7, 6, 1, 2, 3, 4]
id(l)
1972326037376
l.append(5)
l
[10, 9, 7, 6, 1, 2, 3, 4, 5]
id(l)
1972326037376
l.insert(1,13)
l
[10, 13, 9, 7, 6, 1, 2, 3, 4, 5]
l=extend([52,32,42])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    l=extend([52,32,42])
NameError: name 'extend' is not defined
l.extend({52,32,42])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
l.extend([52,32,42])
l
[10, 13, 9, 7, 6, 1, 2, 3, 4, 5, 52, 32, 42]
id(l)
1972326037376
l.pop()
42
l
[10, 13, 9, 7, 6, 1, 2, 3, 4, 5, 52, 32]
l.pop()
32
l
[10, 13, 9, 7, 6, 1, 2, 3, 4, 5, 52]
l.pop(1)
13
l
[10, 9, 7, 6, 1, 2, 3, 4, 5, 52]
id(l)
1972326037376
l.remove([10])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    l.remove([10])
ValueError: list.remove(x): x not in list
l.remove(10)
l
[9, 7, 6, 1, 2, 3, 4, 5, 52]
l.clear()
l
[]
l=[10, 9, 7, 6, 1, 2, 3, 4, 5, 52]
l
[10, 9, 7, 6, 1, 2, 3, 4, 5, 52]
max(l)
52
min(l)
1
sorted(l)
[1, 2, 3, 4, 5, 6, 7, 9, 10, 52]
l
[10, 9, 7, 6, 1, 2, 3, 4, 5, 52]
l.reverse()
l
[52, 5, 4, 3, 2, 1, 6, 7, 9, 10]
l.sort()
l
[1, 2, 3, 4, 5, 6, 7, 9, 10, 52]
l=[1,2,3,4]
m=[1,2,3,4]
l+m
[1, 2, 3, 4, 1, 2, 3, 4]
l
[1, 2, 3, 4]
m
[1, 2, 3, 4]
l.sort(reverse=True)
l
[4, 3, 2, 1]
sum(1)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    sum(1)
TypeError: 'int' object is not iterable
sum(l)
10
m=l.copy()
m.append(4)
l
[4, 3, 2, 1]
m
[4, 3, 2, 1, 4]
>>> l
[4, 3, 2, 1]
>>> all([1,'',[],(),set(),{},False])
False
>>> all([0,'',[],(),set(),{},False])
False
>>> any([1,'',[],(),set(),{},False])
True
>>> l
[4, 3, 2, 1]
>>> l.index(3)
1
>>> l
[4, 3, 2, 1]
>>> l.count(4)
1
>>> l
[4, 3, 2, 1]
>>> l=[[1,2,3,4],[5,6,7,8]]
>>> l
[[1, 2, 3, 4], [5, 6, 7, 8]]
>>> l[0]
[1, 2, 3, 4]
>>> l[1]
[5, 6, 7, 8]
>>> l[0][2]
3
>>> l[1][3]
8
>>> l[-1][-1]
8
>>> t=()
>>> t=tuple()
>>> t=(1,12.3,3+5j,"str",[1,2,3],(1,2,3),{1,2},{1:1},True)
>>> t
(1, 12.3, (3+5j), 'str', [1, 2, 3], (1, 2, 3), {1, 2}, {1: 1}, True)
>>> t=(1,2,3,4,4,4,4,4)
>>> t
(1, 2, 3, 4, 4, 4, 4, 4)
