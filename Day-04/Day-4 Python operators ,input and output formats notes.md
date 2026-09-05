### **Day-4 Python operators and output formats**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

##### &#x20;**Python operators:**

&#x20;**-----------------------------**

##### Operators are special symbols or keywords in Python that perform operations on variables and values.  



##### 1\. Arithmetic Operators :used to perform mathematical calculations.

##### &#x20;             a=5,b,3     

&#x20;             

##### &#x20;     + (Addition): Adds two numbers. ex:5+3=8

##### 

##### &#x20;     - (Subtraction): Subtracts one number from another. ex:5-3=2

##### 

##### &#x20;     \* (Multiplication): Multiplies two numbers. ex:5\*3=15

##### 

##### &#x20;     / (Division): Divides two numbers and returns a  floating-point (decimal) value. ex:5/3=1.5

##### 

##### &#x20;    // (Floor Division): Divides two numbers and returns only the integer part. ex:5//3=1

##### 

##### &#x20;    % (Modulus): Returns the remainder after division.  ex:5%3=2



##### &#x20;   \*\* (Exponentiation): Raises a number to the power of another number.  ex:5\*\*3=125

##### 

##### 2\. Comparison Operators: Comparison operators compare two values and return either True or False.

##### 

##### &#x20;       == : Equal to                       | ex: 5 == 5   # True|

##### &#x20;           

##### &#x20;       != : Not equal to                   | ex: 5 != 3   # True|

##### 

##### &#x20;       > : Greater than                    | ex: 7 > 3    # True|

##### 

##### &#x20;       < : Less than                       | ex: 3 < 7    # True|

##### 

##### &#x20;       >= : Greater than or equal to       | ex: 5 >= 5   # True|

##### 

##### &#x20;       <= : Less than or equal to          | ex: 3 <= 5   # True|

##### 

##### 3\. Assignment Operators : Assignment operators are used to assign values to variables or update their values.

##### 

##### &#x20;    = : Assigns a value.                       x = 5

##### 

##### &#x20;    += : Adds and assigns.                     x += 3   (x = x + 3)

##### 

##### &#x20;    -= : Subtracts and assigns.                x -= 2

##### 

##### &#x20;    \*= : Multiplies and assigns.               x \*= 4

##### 

##### &#x20;    /= : Divides and assigns.                  x /= 2

##### &#x20;

##### &#x20;    //= : Floor divides and assigns.           x //= 3

##### 

##### &#x20;    %= : Finds remainder and assigns.          x %= 2

##### 

##### &#x20;   \*\*= : Raises to a power and assigns.        x \*\*= 3



##### &#x20;   \&=, |=, ^=, >>=, <<= : Used with bitwise operations.

##### 

##### &#x20;   := : Walrus operator. Assigns a value inside an expression.

##### 

##### 4\. Logical Operators: Logical operators combine two or more conditions.

##### 

##### &#x20;   i)and   ii)or   iii)not

##### 

##### i) --->  Returns True only if both conditions are True.

##### 

##### &#x20;                    Truth Table

&#x20;                             ----------------------------

##### 

##### &#x20;                  A    |  B    |  A and B

##### &#x20;                 True  | True  |  True

##### &#x20;                 True  |False  |  False

##### &#x20;                 False | True  |  False

##### &#x20;                 False | False |  False



#### ii)---> Returns True if at least one condition is True.

##### 

##### &#x20;                       Truth Table

##### 

##### &#x20;                   A   |   B   |   A or B

##### &#x20;                  True | True  |   True

##### &#x20;                  True | False |   True

##### &#x20;                  False| True  |   True

##### &#x20;                  False| False |   False



##### iii)---> Reverses the result.

##### 

##### &#x20;                       Truth Table

##### 

##### &#x20;                       A   |  not A

##### &#x20;                     True  | False

##### &#x20;                     False | True

##### 

##### 5\. Membership Operators: check whether a value exists in a sequence such as a list, tuple, string, or set.

##### 

##### &#x20;  in : Return **True** if the value exists

##### 

##### &#x20;    ex: "apple" in \["apple", "banana"]   # True



##### &#x20;  not in: Returns True if the value does not exist.

##### 

##### &#x20;    ex:"grape" not in \["apple", "banana"]   # True

##### 

##### 6\. Identity Operators: check whether two variables refer to the same object in memory.

##### 

##### &#x20;   is: Returns **True** if both variables refer to the **same** object.

##### 

##### &#x20;   is not: Returns **True** if they refer to **different** objects.

##### 

##### Ex:

##### a = \[1, 2, 3]

##### b = a

##### c = \[1, 2, 3]

##### 

##### print(a is b)        # True

##### print(a is c)        # False

##### print(a is not c)    # True

##### 

##### 7\. Bitwise Operators: work on the binary (0 and 1) representation of numbers.

##### 

##### &#x20;  x = 5    # Binary: 0101

##### &#x20;  y = 3    # Binary: 0011



##### &#x20; \& (AND)

##### 

##### Returns 1 only if both bits are 1.

##### &#x20;       ex:5 \& 3    # 1

##### &#x20; | (OR)

##### 

##### Returns 1 if at least one bit is 1.

##### &#x20;        ex:5 | 3    # 7

##### &#x20; ^ (XOR)

##### 

##### Returns 1 if the bits are different.

##### &#x20;        ex:5 ^ 3    # 6

##### &#x20; \~ (NOT)



##### Reverses all bits.

##### &#x20;        ex:\~5    # -6

##### << (Left Shift)

##### 

##### Shifts bits to the left. Each shift multiplies the number by 2.

##### &#x20;         ex:5 << 1    # 10

##### >> (Right Shift)

##### 

##### Shifts bits to the right. Each shift divides the number by 2.

##### &#x20;          ex:5 >> 1    # 2



#### &#x20;                                  **Input Formats:**

&#x20;                                                                **------------------------**

##### \---> used to take input from the user during program execution.

##### 

##### Syntax :input("Message")

##### \---> input() always returns a str by default.

##### \---> To get numbers, convert the input using int() or float().



##### 1\. String Input

##### 

##### Used for:

* ##### Name
* ##### City
* ##### Email

##### name = input("Enter your name: ")

##### print(name)



##### 2\. Integer Input

##### 

##### Used for:

* ##### Age
* ##### Marks
* ##### Quantity

##### age = int(input("Enter age: "))

##### print(age)



##### 3\. Float Input

##### 

##### Used for:

* ##### Price
* ##### Temperature
* ##### Rating

##### price = float(input("Enter price: "))

##### print(price)



##### 4\. List of Strings

##### 

* ##### Use .split() to separate words by spaces.

##### 

##### names = input("Enter names: ").split()

##### print(names)

##### 

##### 5\. Tuple of Strings



* ##### names = tuple(input().split())

##### print(names)

##### 

##### 6\. Set of Strings



* ##### names = set(input().split())

##### print(names)

##### 

##### 7\. List of Integers



* ##### numbers = list(map(int, input().split()))

##### print(numbers)

##### 

##### 8\. Tuple of Integers



* ##### numbers = tuple(map(int, input().split()))

##### print(numbers)



##### 9\. Set of Integers

* ##### numbers = set(map(int, input().split()))

##### print(numbers)

##### 

##### 10\. List of Floats



* ##### values = list(map(float, input().split()))

##### print(values)



##### 11\. Tuple of Floats



* ##### values = tuple(map(float, input().split()))

##### print(values)



##### 12\. Set of Floats



* ##### values = set(map(float, input().split()))

##### print(values)

##### 

##### &#x20;\*Duplicates are removed.

##### 

##### 13\. Using eval()

##### 

* ##### eval() converts Python expressions into their actual data types.

##### 

##### It can accept:

##### 

##### Integer

##### Float

##### String

##### List

##### Tuple

##### Set

##### Dictionary

##### Boolean

##### Dictionary

##### data = eval(input())

##### print(data)

##### 

#### &#x20;                                  **Output Formatting**

&#x20;                                                       **------------------------------------------------**

##### 

* ##### The print() function is used to display output.

##### 

##### &#x20;      Syntax: print(object, sep=' ', end='\\n')

##### &#x20; Parameters:

##### \-----------------

* ##### object → Value to display
* ##### sep → Changes the separator between values.

&#x20;   

##### &#x20;     ex: print("2026", "07", "15", sep="-")

##### 

##### &#x20;         Output: 2026-07-15



* ##### end → Changes what is printed after the output.

##### 

##### &#x20;      ex: print("Hello", end=" ")

##### &#x20;          print("World")

##### 

##### &#x20;      Output: Hello World

* #### Methods

#### \----------------

##### 1\. Using Commas:



##### &#x20;  ex: print("Name:", name, "Age:", age)

##### 

##### 2\. Using % Formatting (Old Style):

##### 

##### &#x20;    Format Specifiers:

* ##### &#x20;      %s → String
* ##### &#x20;      %d → Integer
* ##### &#x20;      %f → Float

##### &#x20;  ex: print("Name: %s Age: %d Score: %.2f" % (name, age, score))

##### 

##### &#x20;    \* %.2f displays 2 decimal places.

##### 

##### 3\. Using f-Strings:

##### &#x20;       ex: print(f"Name: {name} Age: {age} Score: {score:.2f}")

##### 

##### 4\. Using str.format():

##### &#x20;     print("Name: {} Age: {}".format(name, age))

##### &#x20;     Positional Formatting

##### &#x20;     print("Name: {0} Age: {1}".format("Ravi", 25))

##### &#x20;     Keyword Formatting

##### &#x20;     print("Name: {name} Age: {age}".format(name="Ravi", age=25))

##### &#x20;     Number Formatting

##### &#x20;     Comma Separator

##### 

##### 

