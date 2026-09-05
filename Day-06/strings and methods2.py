Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> c='strings.py'
>>> c.startswith()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    c.startswith()
TypeError: startswith expected at least 1 argument, got 0
>>> c.startswith('str')
True
>>> c.startswith('python')
False
>>> c.endswith('py')
True
>>> c.endswith('python')
False
>>> c.islower()
True
>>> c.isupper()
False
>>> 'PYTHONV13'.isupper()
True
>>> c.isaplha()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
>>> c.isalpha()
False
>>> c.isalnum()
False
>>> '    '.isspace()
True
>>> 'Python Is Title'.istitle()
True
>>> 'my@var'.isidentifier()
False
>>> 'my_var'.isidentifier()
True
>>> l[]
SyntaxError: invalid syntax
