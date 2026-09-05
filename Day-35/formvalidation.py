#name form
'''
import re
fullname = input("Enter the full name: ")
pattern = r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res = re.fullmatch(pattern,fullname)
print("Valid full name" if res else "Invalid full name")
'''
#email
'''
import re
email = input("Enter the email: ")
pattern = r'^[A-Za-z0-9._]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}$'
res = re.fullmatch(pattern,email)
print("Valid email" if res else "Invalid email")
'''
#phone number
'''
import re
phonenumber = (input("Enter the number: "))
pattern = r'^(?:\+91|0)?[6-9]\d{9}$'  r'^(?:\+91\s?|0)?[6-9]\d{9}$'
res = re.fullmatch(pattern,phonenumber)
print("Valid phonenumber" if res else "Invalid phonenumber")
'''
# password
'''
import re
password = input("Enter the password: ")
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
res = re.fullmatch(pattern,password)
print("Valid password" if res else "Invalid password")
'''
#username

import re
username = (input("Enter the username: "))
pattern = r'^[A-Za-z0-9_.]{5,25}$'
res = re.fullmatch(pattern,username)
print("Valid username" if res else "Invalid username")

#aadhar number

import re
aadhar = input("Enter the number: ")
pattern = r'^\d{4}\s?\d{4}\s?\d{4}$'
res = re.fullmatch(pattern,aadhar)
print("Valid aadhar" if res else "Invalid aadhar")
