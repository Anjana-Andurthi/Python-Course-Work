                                                          Day-5 Strings
Introduction to Strings
-------------------------
A string is a sequence of characters enclosed in:
-->Single quotes: 'Hello'
-->Double quotes: "Hello"
-->Triple quotes: '''Hello''' or """Hello"""
-->Strings are immutable(meaning they cannot be changed after creation.)

    Ex:
        s1 = "Hello"
        s2 = 'Python'
        s3 = """Multi-line
                String"""
  String Operations:
-----------------------
1. Concatenation (+):
-->Joins two or more strings.
            Ex:"Hello" + " World"=Hello World

2. Repetition (*):
-->Repeats a string.
                Ex:"Hi " * 3= Hi Hi Hi

3. Indexing:
-->Accesses characters using index.
                Ex:text = "Python"
                   text[0]    # P
                   text[-1]   # n
4. Slicing:
-->Extracts part of a string.
                Ex:text[0:3]   # Pyt
                   text[:4]    # Pyth
                   text[2:]    # thon
5. Membership (in, not in)
-->Checks whether a substring exists.
                Ex:"Py" in text       # True
                   "Java" not in text # True
Built-in String Functions:
----------------------------
                    Function              	     Purpose
                     len()	                   Returns length
                     max()	                   Highest ASCII character
                     min()	                   Lowest ASCII character
                     sorted()	               Returns sorted list of characters
                     ord()	                   Character → ASCII value
                     chr()	                   ASCII value → Character

       Example:
               len("Hello")       # 5
               ord('A')           # 65
               chr(97)            # a
               sorted("python")   # ['h','n','o','p','t','y']

                    String Methods:
                -----------------------
1. Case Conversion:
                upper()      → Uppercase
                lower()      → Lowercase
                capitalize() → First letter capital
                title()      → First letter of every word capital
                swapcase()   → Swap upper/lower case
                casefold()   → Strong lowercase

2. Alignment & Formatting:
-->center()
-->ljust()
-->rjust()
-->zfill()

3. Search Methods:
               find()   → Returns index or -1
               rfind()  → Last occurrence
               index()  → Like find(), but error if not found
               rindex() → Last occurrence, error if not found
               count()  → Counts occurrences

4. Testing Methods (Return True/False):
-->startswith()
-->endswith()
-->isalpha()
-->isalnum()
-->islower()
-->isupper()
-->isspace()
-->istitle()
-->isidentifier()
-->isdecimal()
-->isdigit()
-->isnumeric()
Difference:
-->isdecimal() → Only decimal digits (0–9)
-->isdigit() → Decimal + superscript digits
-->isnumeric() → Digits, fractions, Roman numerals, Unicode numbers

5. Replace & Modify:
-->replace(old, new)
-->translate(table)
-->maketrans()

6. Splitting & Joining:
-->split()
-->rsplit()
-->splitlines()
-->join()
-->partition()
-->rpartition()

7. Whitespace Methods:
-->strip()
-->lstrip()
-->rstrip()

8. Encoding & Decoding:
-->encode() → String to bytes
-->decode() → Bytes to string
            Ex:text = "Hello"
               text.encode("utf-8")
               b'Hello'.decode("utf-8")                                                         