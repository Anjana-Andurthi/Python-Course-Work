## &#x20;                   **Day-3 DataTypes and Typeconversions**

### &#x20;                   \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

#### &#x20;                                 **DATATYPES:**

##### Python data types are classified into:

##### 

1. ##### Numeric Types
2. ##### Sequence Types
3. ##### Set Types
4. ##### Mapping Type
5. ##### Boolean Type
6. ##### None Type



##### 1\. Numeric Types: Numeric data types are used to store numerical values.

##### 

##### Characteristics:

* ##### Store numbers.
* ##### Optimized for mathematical calculations.
* ##### Stored internally in binary format.
* ##### Immutable (cannot be modified after creation).

### Types:

##### a) int: Stores whole numbers without decimal values.

##### b) float: Stores decimal numbers.

##### c) complex: Stores real and imaginary numbers.

##### &#x20;      Used in Scientific calculations, Engineering, Signal processing



#### 2\. Sequence Types: Sequence data types store multiple values in a specific order.

##### &#x20;    Characteristics:

* ##### Ordered collection.
* ##### Supports indexing.
* ##### Immutable.
* ##### Can be traversed using loops.

#### &#x20;  Types:



##### a) str: Stores text.

##### &#x20;       ex: name = "Codegnan"



##### b) list: Stores multiple values in an ordered collection.(mutable)

##### 

##### &#x20;        ex: numbers = \[10, 20, 30]

##### Why Mutable?

##### \--->Elements inside a list can be added, removed, or modified after creation.

##### 

##### c) tuple

##### 

##### Stores ordered fixed data.

##### 

##### data = (10, 20, 30)

##### 

##### Characteristics:

##### 

* ##### Ordered.
* ##### Indexed.
* ##### Allows duplicates.
* ##### Faster than lists.
* ##### Immutable.



##### 3\. Set Types: Set data types store unique values.

##### &#x20;  Types:



##### a) set

##### colors = {"Red", "Blue", "Green"}

##### 

##### Characteristics:

* ##### Stores unique values only.
* ##### Removes duplicates automatically.
* ##### Unordered.
* ##### Mutable.



##### Example: {"Nike", "Puma", "Nike"} becomes {"Nike", "Puma"}



##### b) frozenset: Immutable version of a set.

##### 

##### tags = frozenset(\["Sale", "Trending"])

##### 

##### Characteristics:

* ##### Unique values only.
* ##### Cannot be modified.
* ##### Immutable.



##### 4\. Mapping Type:



* ##### dict (Dictionary): A dictionary stores data in key–value pairs.

##### 

##### &#x20; Characteristics:

* ##### Stores data as key and value.
* ##### Mutable.
* ##### Ordered (Python 3.7+).
* ##### Duplicate keys are not allowed.
* ##### Uses hashing for fast searching.



##### 5\. Boolean Type: Stores only two values:

##### 

* ##### True
* ##### False

##### 

##### Used for:

* ##### Conditions
* ##### Decision making
* ##### Comparisons



##### 6\. None Type: Represents the absence of a value.



##### Used when:

* ##### Value is not assigned.
* ##### Placeholder is required.
* ##### Empty state.



##### Characteristics:



* ##### Python has only one None object.
* ##### Immutable.



##### Mutable vs Immutable Data Types

\--------------------------------------------------

##### Mutable Data Types: the value can be changed after creation.

##### 

##### &#x20;            Examples:

##### &#x20;                    -->  list

##### &#x20;                    -->  set

##### &#x20;                    -->  dict

##### Immutable Data Types: the value cannot be changed after creation.

##### 

##### &#x20;            Examples:

##### 

##### &#x20;                     -->  int

##### &#x20;                     -->  float

##### &#x20;                     -->  str

##### &#x20;                     -->  tuple

##### &#x20;                     -->  frozenset

##### &#x20;                     -->  bool

##### &#x20;                     -->  NoneType

##### 

##### Ordered vs Unordered Data Types

\---------------------------------------------------

##### Ordered Data Types: Elements maintain the order in which they are inserted.

##### 

##### &#x20;           Examples:

##### 

##### &#x20;                      -->   list

##### &#x20;                      -->   tuple

##### &#x20;                      -->   str

##### &#x20;                      -->   dict (Python 3.7+)

##### Unordered Data Types: Elements do not have a fixed order.

##### 

##### &#x20;           Examples:

##### 

##### &#x20;                      -->  set

##### &#x20;                      -->  frozenset

##### Indexed vs Non-Indexed Data Types

\-------------------------------------------------------

##### Indexed Data Types: Elements can be accessed using their position (index).

##### 

##### &#x20;           Examples:

##### 

##### &#x20;                      -->  list

##### &#x20;                      -->  tuple

##### &#x20;                      -->  str

##### 

##### Non-Indexed Data Types: Elements cannot be accessed using indexes.

##### 

##### &#x20;           Examples:

##### 

##### &#x20;                      -->  set

##### &#x20;                      -->  frozenset

##### &#x20;                      -->  dict

##### 

### &#x20;                                 **Type Conversions**

&#x20;                                                           **---------------------------------------------**

##### 1\. int (Integer):

* ##### Stores whole numbers.

##### &#x20; Ex: 10, -5, 100

##### &#x20; int convert--> float, complex, str, bool

##### &#x20; Cannot convert--> list, tuple, set, frozenset, dict

##### 2\. float:

* ##### Stores decimal numbers.

##### &#x20; Ex: 10.5, 3.14

##### &#x20; convert-->int, complex, str, bool

##### &#x20; cannot convert directly-->list, tuple, set, frozenset, dict

##### 3\. complex:

* ##### Stores numbers with a real and imaginary part.

##### &#x20; Ex: 5+2j

##### &#x20; Can convert-->str, bool

##### &#x20; Cannot convert-->int, float, list, tuple, set, frozenset, dict

##### 4\. str (String):

* ##### Stores text.

##### &#x20; Ex: "Python", "100"

##### &#x20; Can convert to-->int, float, complex, list, tuple, set, frozenset, bool

##### &#x20; Cannot convert-->dict 

##### 5\. bool (Boolean):

* ##### Represents logical values.(True,false)

##### &#x20; Can convert to-->int, float, complex, str

##### &#x20; Cannot convert-->list, tuple, set, frozenset, dict

##### 6\. list:

* ##### Ordered and mutable collection.

##### &#x20; Example: \[1, 2, 3]

##### &#x20; Can convert-->str, bool, tuple, set, frozenset, dict 

##### &#x20; Cannot convert to-->int, float, complex

##### 7\. tuple:

* ##### Ordered and immutable collection.

##### &#x20; Example: (1, 2, 3)

##### &#x20; Can convert-->str, bool, list, set, frozenset, dict 

##### &#x20; Cannot convert-->int, float, complex

##### 8\. set:

* ##### Unordered collection of unique elements.

##### &#x20; Example: {1, 2, 3}

##### &#x20; Can convert-->str, bool, list, tuple, frozenset, dict 

##### &#x20; Cannot convert-->int, float, complex

##### 9\. frozenset:

* ##### Immutable version of a set.

##### &#x20; Example: frozenset({1, 2})

##### &#x20; Can convert-->str, bool, list, tuple, set, dict 

##### &#x20; Cannot convert-->int, float, complex

##### 10\. dict :

* ##### Stores data in key:value pairs.

##### &#x20; Example: {"a": 1, "b": 2}

##### &#x20; Can convert-->str, bool, list, tuple, set, frozenset, dict

##### &#x20; Converting to list, tuple, set, or frozenset returns only the keys.

##### &#x20; Cannot convert-->int, float, complex

##### 

