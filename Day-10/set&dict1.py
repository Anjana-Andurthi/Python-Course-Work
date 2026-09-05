Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
data={'name':'Anjana','batch':63,'course':'PFS'}
data['name']
'Anjana'
data['batch']
63
data['course']
'PFS'
63 in data
False
data['age']
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    data['age']
KeyError: 'age'
data.get('age','key is not present')
'key is not present'
data.get('course','key is not present')
'PFS'
data['batch']=64
data
{'name': 'Anjana', 'batch': 64, 'course': 'PFS'}
data['skills']=['python','mysql','flask']
data
{'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask']}
data['age']=21
data
{'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21}
data.update({'phno':9876543210,'email':'anjanaandurthi@gmail.com'})
data
{'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'anjanaandurthi@gmail.com'}
data.pop()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data.pop()
TypeError: pop expected at least 1 argument, got 0
data.pop('age')
21
data
{'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210, 'email': 'anjanaandurthi@gmail.com'}
data.popitem()
('email', 'anjanaandurthi@gmail.com')
data
{'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210}
del.data['name']
SyntaxError: invalid syntax
del data['name']
data
{'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210}
data.clear()
data
{}
data={'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21}
data.update({'phno':9876543210,'email':'anjanaandurthi@gmail.com'})
SyntaxError: multiple statements found while compiling a single statement
data={'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'anjanaandurthi@gmail.com'}
data
{'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'anjanaandurthi@gmail.com'}
data.keys()
dict_keys(['name', 'batch', 'course', 'skills', 'age', 'phno', 'email'])
data.values()
dict_values(['Anjana', 64, 'PFS', ['python', 'mysql', 'flask'], 21, 9876543210, 'anjanaandurthi@gmail.com'])
data.items()
dict_items([('name', 'Anjana'), ('batch', 64), ('course', 'PFS'), ('skills', ['python', 'mysql', 'flask']), ('age', 21), ('phno', 9876543210), ('email', 'anjanaandurthi@gmail.com')])
sorted(data)
['age', 'batch', 'course', 'email', 'name', 'phno', 'skills']
sorted(data,reverse=True)
['skills', 'phno', 'name', 'email', 'course', 'batch', 'age']
max(data)
'skills'
min(data)
'age'
data
{'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'anjanaandurthi@gmail.com'}
data['age']
21
>>> 21data.get('age')
SyntaxError: invalid decimal literal
>>> data.get('age')
21
>>> data
{'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'anjanaandurthi@gmail.com'}
>>> {'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210}
{'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'phno': 9876543210}
>>> data.get('age')
21
>>> data
{'name': 'Anjana', 'batch': 64, 'course': 'PFS', 'skills': ['python', 'mysql', 'flask'], 'age': 21, 'phno': 9876543210, 'email': 'anjanaandurthi@gmail.com'}
>>> len(data)
7
>>> all(data)
True
>>> any(data)
True
>>> a={1:1,2:2}
>>> a
{1: 1, 2: 2}
>>> b={1:1,2:2,3:3}
>>> b
{1: 1, 2: 2, 3: 3}
>>> \
...   c=a.copy()
SyntaxError: unexpected indent
>>> c=a.copy()
>>> c
{1: 1, 2: 2}
>>> c[4]=4
>>> c
{1: 1, 2: 2, 4: 4}
>>> a
{1: 1, 2: 2}
>>> d=dict.fromkeys(["a","b"])
d=dict.fromkeys(["a","b"],0)
d
{'a': 0, 'b': 0}
