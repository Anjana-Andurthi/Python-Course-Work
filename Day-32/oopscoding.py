class User:
    def __init__(self,name,email,phone,password):
        self.name=name
        self.email=email
        self.phone=phone
        self.password=password
    def register(self):
        if not self.name:
            print("Registration Failed: name is required")    
        elif not self.email:
            print("Registration Failed: email is required")
        elif not self.phone:
            print("Registration Failed: phone is required")
        elif not self.password:
            print("Registration Failed: password is required")    
        else:
            print("Registration Successful")  

name=input("Name:") 
email=input("Email:") 
phone=int(input("Phone:"))
password=(input("Password:"))  

user= User(name,email,phone,password)
user.register()