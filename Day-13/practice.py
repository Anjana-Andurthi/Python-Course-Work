# Positive or Negative
'''
n=int(input("Enter the number: "))
if n>0:
    print("Postive Number")
else:
    print("Negative Number")  
'''
#Even r Odd
'''
n=int(input("Enter the Number: "))  
if n%2==0:
    print("Even Number")
else:
    print("Odd Number")  
'''
#Divisible by 5
'''
n=int(input("Enter the number: ")) 
if n%5==0:
    print("Divisible By 5")
else:
    print("Not Divisible by 5")  
'''      
#Divisible by 3 & 7  
''' 
n=int(input("Enter the number: ")) 
if n % 3 and n % 7 ==0:
    print("Divisible by both 3 and 7") 
else:
    print("Not divisible by both 3 and 7")
'''
#Leap Year
'''
n=int(input("Enter the number: "))
if n % 4 ==0 or n % 400 == 0 and n % 100 !=0:
    print("Leap Year")       
else:
    print("Not a leap year") 
'''
# check pass r fail
'''
n=int(input("Enter the marks: "))
if n>=35:
    print("Pass")
else:
    print("Fail")    
'''
#check if number is 3-digit
'''
num=int(input("Enter the digit: "))
if (100<=num<=999) or (-999<=num<=-100):
    print("3-digit number")
else:
    print("Not a 3-digit number")   
 '''
#Check if char is vowel
'''
ch=input("Enter the character: ")
if ch in 'aeiouAEIOU':
    print("is vowel")
else:
    print("is not vowel")  
'''
# check greatest of 2 numbers
'''
a=int(input("Enter the 1st number: "))
b=int(input("Enter the  2nd number: "))
if a>b:
    print( f"{a} is greater" )
else:
    print(f"{b} is greater")            
'''
#smallest of two numbers
'''
a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
if a<b:
    print(f"{a} is smaller")
else:
    print(f"{b} is smaller") 
'''
#if number is zer0
'''
n=int(input())
if n==0:
    print("Number is zero")
else:
    print("not a zero") 
'''
#number is multiple of 10
'''
n=int(input("enter the number:"))
if n%10==0:
    print("Multiple of 10")
else:
    print("Not a multiple") 
'''
#eligible to vote
'''
age=int(input("Enter the Age: ")) 
if age>=18:
    print("Eligible to vote") 
else:
    print("Not Eligible")
'''
#number btwn 1 and 100
'''
num=int(input("Enter the number: "))
if 1<=num<=100:
    print("In range of 1 and 100")
else:
    print("Not in range")
'''
#square of another
'''
a=int(input())
b=int(input())
if a==b*b:
    print("Yes")  
else:
    print("no") 
'''
# 2 strings are equal
'''
str1=input("Enter the string: ")       
str2=input("Enter the string: ")
if str1==str2:
    print("Strings are Equal")
else:
    print("Strings are not equal") 
'''
#positive and even
'''
num=int(input("Enter the number: ")) 
if num>0 and num%2==0:
    print("Positive and even number")
'''
#Uppercase
'''
char=input("Enter the char: ")
if char.isupper():
    print("Uppercase letter")
'''
#temp is hot(>30)
'''
temp=int(input("Enter the temp: "))
if temp>30:
    print("Its hot")
else:
    print("its not hot") 
'''
#4-digit even number
'''
num=int(input("Enter the 4-digit number: "))
if num>999 and num%2==0:
    print("4-digit even number")
'''
#char is consonant
'''
char=input("Enter the char:")
if char not in 'aeiouAEIOU':
    print("Consonant") 
else:
    print("not a consonant") 
'''
#divisible by 2 and 3 but not both
'''
num=int(input("Enter the number:"))
if num%2==0 and num%3!=0:
    print("Divisible by 2 only")
elif num%3==0 and num%2!=0:
    print("Divisible by 3 only") 
else:
    print("not valid")
'''
#negative and odd
'''
n=int(input("Enter the number: "))
if n<0 and n%2!=0:
    print("Negative and Odd")
else:
    print("not valid") 
'''
#string start with a vowel
'''
ch=input("Enter the string: ")
if ch[0] in 'aeiouAEIOU':
    print("Starts with a Vowel")
'''
#three sides form a valid triangle
'''
a=int(input())
b=int(input())
c=int(input())
if a+b>c and b+c>a and c+a>b:
    print("Valid Triangle")
'''
#greatest among 3 numbers
'''
a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
'''
#century yr and leap yr
'''
year = int(input())

if year % 100 == 0 and year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century year but not a leap year")
elif year % 4 == 0:
    print("Leap year")
else:
    print("Not a leap year")
'''
#char is a digit
'''
ch = input()

if ch.isdigit():
    print("Digit")
else:
    print("Not a digit")
'''
#palindrome
'''
s = input()
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
'''
#compare lengths of two strings
'''
str1 = input("Enter the string: ")
str2 = input("Enter the strings: ")
if len(str1) > len(str2):
    print("First string is longer")
elif len(str1) < len(str2):
    print("Second string is longer")
else:
    print("Both strings are of equal length")
'''
#specific range(50 to 100) and divisible by 5                         
'''
num = int(input())
if 50 <= num <= 100 and num % 5 == 0:
    print("Valid")
else:
    print("Invalid")
'''
#password length is strong
'''
password = input("Enter the password: ")
if len(password) > 8:
    print("Strong password")
else:
    print("Weak password")
'''
#sum of two numbers is even
'''    
a = int(input())
b = int(input())
if (a + b) % 2 == 0:
    print("Sum is even")
else:
    print("Sum is odd")
'''
#character is a special symbol (!, @, #, etc.)    
'''
ch = input()
if not ch.isalnum():
    print("Special symbol")
else:
    print("Not a special symbol")
'''
#temperature is cold (<15°C), moderate (15–30°C), or hot (>30°C)    
'''
temp = float(input())
if temp < 15:
    print("Cold")
elif 15 <= temp <= 30:
    print("Moderate")
else:
    print("Hot")
'''
#number lies outside the range 10 to 50
'''
num = int(input())
if num < 10 or num > 50:
    print("Outside the range")
else:
    print("Inside the range") 
'''
#perfect square
'''
num = int(input())
root = int(num ** 0.5)
if root * root == num:
    print("Perfect square")
else:
    print("Not a perfect square")
'''
# two ages and determine who is older or if same age
'''          
age1 = int(input("Enter the age: "))
age2 = int(input("Enter the age: "))
if age1 > age2:
    print("First person is older")
elif age2 > age1:
    print("Second person is older")
else:
    print("Both are of the same age")
'''
# angle is acute, right, or obtuse
'''
angle = int(input("Enter the angle: "))

if angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
elif angle < 180:
    print("Obtuse angle")
else:
    print("Invalid angle")
'''       