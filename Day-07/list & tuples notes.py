
                       DAY-6 LISTS And TUPLES
 -----------------------------------------------------------------------------      

LISTS:
-->A list is an ordered, mutable collection of elements.
-->Created using [] or list().
-->Can store different data types.

Example:lst = [10, "Python", 5.5, True]

List Properties:

  ✅ Ordered
  ✅ Mutable (can be changed)
  ✅ Indexed
  ✅ Iterable
  ✅ Allows duplicates
  ✅ Dynamic size
  ✅ Heterogeneous (different data types)
  
List Operations:

-->Concatenation (+) - Joins lists
-->Repetition (*)    - Repeats elements
-->Indexing          - Access elements using index
-->Slicing           - Extract part of a list
-->Membership        - in, not in

Built-in Functions:

-->len()    – Length
-->max()    – Largest element
-->min()    – Smallest element
-->sum()    – Sum of elements
-->sorted() – Returns sorted list
-->list()   – Converts iterable to list

Important List Methods:

1)Adding:
-->append()
-->extend()
-->insert()
2)Removing:
-->remove()
-->pop()
-->clear()
-->del
3)Searching:
-->index()
-->count()
4)Sorting:
-->sort()
-->reverse()
-->sorted()
5)Copying:
-->copy()
6)Nested List:
-->A list inside another list.
     Ex:data = [[1, 2], [3, 4]]
        print(data[1][1])   # 4

    TUPLES:
----------------
-->A tuple is an ordered, immutable collection.
-->Created using () or tuple().
-->Can store different data types.
   Example: t = (10, "Python", 5.5, True)

Tuple Properties:
✅ Ordered
✅ Immutable (cannot be modified)
✅ Indexed
✅ Iterable
✅ Allows duplicates
✅ Heterogeneous
✅ Faster and uses less memory than lists
Creating Tuples
t = ()
t = (10,)      # Single-element tuple

Tuple Operations:
-->Concatenation (+)
-->Repetition (*)
-->Indexing
-->Slicing
-->Membership (in, not in)

Built-in Functions:
-->len()
-->max()
-->min()
-->sum()
-->sorted() (returns a list)
-->tuple()
-->any()
-->all()

Tuple Methods:

-->count()
-->index()
-->Tuple Packing
      Ex:data = 10, 20, 30
-->Tuple Unpacking
      Ex:a, b, c = (10, 20, 30)
-->Nested Tuple
      Ex:data = ((1, 2), (3, 4))
         print(data[1][1])   # 4
-->Mutable Object Inside Tuple:
A tuple cannot change, but mutable objects (like lists) inside it can.
          Ex:data = (10, [20, 30], 40)
             data[1].append(50)
Why Use Tuples?
-->Fixed data
-->Faster than lists
-->Memory efficient
-->Supports packing & unpacking
-->Can be used as dictionary keys (if all elements are immutable)
                         
                         List vs Tuple 
                  --------------------------------       
          Feature	                 List	                         Tuple
           Syntax                 	[]                          	()
           Mutability	            Mutable	                     Immutable
           Add/Remove              	Yes	                          No
           Modify	                  Yes	                          No
           Ordered	                Yes	                          Yes
           Indexed	                Yes	                          Yes
           Duplicates	              Yes	                          Yes
           Dynamic Size	            Yes	                          No
           Memory	                  More	                        Less
           Speed	                  Slower	                      Faster
           Methods	                Many	                    Only count(), index()
           Dictionary Key	          No	                       Yes (if immutable)