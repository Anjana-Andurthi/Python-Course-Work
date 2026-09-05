Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 20
b = 10
a+b
30
a-b
10
a*b
200
a/b
2.0
a//b
2
b**a
100000000000000000000
a**b
10240000000000
a%b
0
4**2
16
a = 20
b = 10
a<b
False
a>b
True
a<=b
False
a>=b
True
a!=b
True
a==b
False
c=10
c +=10
c=10
c = c+10
c=c+10
c = 10
c = c+10
c
20
c+=10
c
30
c-=10
c
20
c*=2
c
40
c//=2
c
20
c/=2
c
10.0
c%=2
c
0.0
c**=2
c
0.0
True and True
True
True and False
False
n = 10
n%2==0
True
n%2==0 and n%3==0
False
n%2== or n%3==0
SyntaxError: invalid syntax
n%2==0 or n%3==0
True
n
10
n<5
False
not n>5
False
not n<8
True
#str list tuple set dict
s="codegnan"
"ë" in s
False
"e" in s
True
"n" in s
True
8 in s
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    8 in s
TypeError: 'in <string>' requires string as left operand, not int
"8" in s
False
l=[1,2,3,4,5]
4 in l
True
6 in l
False
8 not in l
True
t=(1,2,3,4,5)
2 in t
True
5 in t
True
6 not in t
True
s =(9,8,7,6,5)
4 not in s
True
9 in s
True
6 in s
True
d=("name":"Anjana","batch":63,"course":"python")
SyntaxError: invalid syntax
d={"name":"Anjana","batch":63,"course":"python"}
A in d
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    A in d
NameError: name 'A' is not defined. Did you mean: 'a'?
a in d
False
63 in d
False
b in d
False
c in d
False
name in d
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    name in d
NameError: name 'name' is not defined
"name" in d
True
"python" in d
False
#identity operators
l=[1,2,3,4]
m=[1,2,3,4]
id(l)
3088154952896
id(m)
3088154953024
l is m
False
l is not m
True
n=l
id(n)
3088154952896
l is n
True
#mutable and immutable
s="codegnan"
id(s)
3088154956528
s="codegnan ciurses"
id(s)
3088155004592
s
'codegnan ciurses'
set=[1,2,3,4,5]
s
'codegnan ciurses'
set
[1, 2, 3, 4, 5]
id(set)
3088155002816
set.add(6)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    set.add(6)
AttributeError: 'list' object has no attribute 'add'
set.append(6)
set
[1, 2, 3, 4, 5, 6]
id(set)
3088155002816
set={1,2,3,4,5}
set
{1, 2, 3, 4, 5}
id(set)
3088152561472
set.add(6)
set
{1, 2, 3, 4, 5, 6}
id(set)
3088152561472
#bitwise
9&10
8
9|10
11
9^10
3
8>>2
2
8<<2
32
>>>  #output formats
>>> a=10
>>> b=10.5
>>> c="codegnan"
>>> print(a,b,c)
10 10.5 codegnan
>>> print("a value is",a)
a value is 10
>>> print("a value is",a,"| b value is",b,"| c value is",c)
a value is 10 | b value is 10.5 | c value is codegnan
>>> print(a,b,c)
10 10.5 codegnan
>>> print(a,b,c,sep="")
1010.5codegnan
>>> print(a,b,c,sep="\n")
10
10.5
codegnan
>>> print(a,b,c,sep="\t")
10	10.5	codegnan
>>> print(a,b,c,sep="\t",end="@")
10	10.5	codegnan@
>>> print(a,b,c,sep="\t",end="\n\n")
10	10.5	codegnan

>>> print(f"a={a},b={b},c={c}")
a=10,b=10.5,c=codegnan
>>> print("a=%d b=%f c=%s" %(a,b,c))
a=10 b=10.500000 c=codegnan
>>> print("a=%d b=%2f c=%s" %(a,b,c))
a=10 b=10.500000 c=codegnan
>>> print("a={} | b={} | c={}".format(a,b,c))
a=10 | b=10.5 | c=codegnan
>>> print("a={} | b={} | c={}".format(c,a,b))
a=codegnan | b=10 | c=10.5
>>> a=codegnan | b=10 | c=10.5
SyntaxError: cannot assign to expression
>>> print("a={1} | b={2} | c={0}".format(a,b,c))
a=10.5 | b=codegnan | c=10
