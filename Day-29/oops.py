class Flipkart:
    products = {'shirts':1000,'handbag':2000,'pants':3000}
    discount=30

    @classmethod
    def display(cls):
        print(cls.products)

    def userinfo(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"Hello {self.name},Welcome to the flipkart")

    @staticmethod
    def displaydiscount():
        print(f"{Flipkart.discount}% discount is going on grab the products ")    

Anjana=Flipkart()
Anjana.userinfo('Anjana',987654321,'Korutla')
Anjana.displaydiscount()
Anjana.display()
print(Anjana.products)
print(Anjana.name)

Flipkart.displaydiscount()
Flipkart.display()
print(Flipkart.products)

#using objects--> ins,class,static,classattribute,instattribute
#using class--> class,static,classattribute

Amani=Flipkart()
Amani.userinfo('Amani',987654321,'Hyd') 
Amani.displaydiscount()
Amani.display()       