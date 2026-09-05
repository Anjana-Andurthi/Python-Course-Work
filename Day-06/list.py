Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l=[]
l[list]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    l[list]
TypeError: list indices must be integers or slices, not type
>>> l=list()
>>> l=[1,12.3,2+3j,'str',[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},None,True]
>>> l
[1, 12.3, (2+3j), 'str', [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, None, True]
>>> l=[1,1,1,1]
>>> l
[1, 1, 1, 1]
>>> type(l)
<class 'list'>
>>> l=[1,2,3,4]
>>> m=[5,6,7]
>>> l+m
[1, 2, 3, 4, 5, 6, 7]
>>> m*3
[5, 6, 7, 5, 6, 7, 5, 6, 7]
>>> l
[1, 2, 3, 4]
>>> l[3]
4
>>> l[-1]
4
>>> l[1:]
[2, 3, 4]
>>> l[:2]
[1, 2]
>>> l[::-1]
[4, 3, 2, 1]
>>>  1 in l
...  
SyntaxError: unexpected indent
>>> 1
1
>>> 1 in l
True
>>> 5 not in l
True
>>> 5 in l
False
