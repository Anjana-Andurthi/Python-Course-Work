Day-2 Tokens,Statements,Identifiers,Comments & Keywords
         Tokens in Python
      ----------------------
Tokens are the smallest units of a Python program. Python has five types of tokens:
1. Keywords : Reserved words in Python (e.g., if, else, while, for, def).
2. Identifiers : Names given to variables, functions, and classes.
3. Literals : Constant values assigned to variables (e.g., 10, "Hello", 3.14).
4. Operators : Symbols that perform operations (e.g., +, -, *, /).
5. Punctuators : Symbols like (), {}, [], ,, :,. used for syntax structuring.
        Statements and Identifiers
      ------------------------------
1.Statement:

A statement is a single line of code that performs an action.

Types of statements:
-->Assignment statement
-->Function call statement
-->Conditional statement (if)
-->Loop statement (for, while)
2. Identifier: An identifier is the name given to:

  -->  Variables
  -->  Functions
  -->  Classes
  -->  Modules
  -->  Objects
3. Rules for Identifiers:
   Rule 1:
          Can contain:
           -->  Letters (A-Z, a-z)
           -->  Digits (0-9)
           -->  Underscore (_)
           ex:user_name
              score1
              total_amount
    Rule 2:
         Cannot start with a digit.   
         ex:1name
    Rule 3:
        Cannot use Python keywords.         
        ex:❌ Invalid
               if = 10
           ✅ Valid
               if_value = 10   
    Rule 4:
        Python is case-sensitive           
        ex:age
           Age
           AGE
      All are different identifiers.
    Rule 5:  
        Special characters are not allowed.
        ex:❌ Invalid
              user-name
              user@name
              price#
    4. Valid and Invalid Identifiers
       Valid:
               name
               user_123
               _temp
               totalAmount
       Invalid:
               1name
               class
               user-name
               @value       
    5. Comments

        Comments explain the code.
        Python ignores comments during execution.

    ---> Single-line comment
         # This is a comment
         x = 10
    ---> Multi-line comment
             '''
             This is a
             multi-line comment
             '''
    6. Keywords

           Keywords are reserved words in Python.
           They have special meanings.
           They cannot be used as variable names.
    Example keywords:
       if
       else
       for
       while
       break
       continue
       class
       def
       return
       import
       True
       False
       None  
    7. Variable 

           A variable is a named memory location used to store data.            
           Syntax (variable_name = value)
    8. Variable Naming Rules
           Must start with a letter or _
           Cannot start with a number
           Can contain letters, digits, and _
           Python is case-sensitive   
    9. Swapping Variables

           Swap two variables without using a temporary variable.  
           a = 5
           b = 10
           a, b = b, a
           print(a, b)       
    10. Deleting Variables

            Use del to delete a variable.

             x = 100
             del x                        