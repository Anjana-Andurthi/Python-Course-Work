#constructor: it is a inst method 
#-->it is special method that is called automatically when object is created
class Flipkart:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        print(f"Hello {self.name},Welcome to Flipkart")

Anjana=Flipkart('Anjana',9876543210)
Amani=Flipkart('Amani',9876567820)        