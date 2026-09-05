from abc import ABC,abstractmethod

class Phonepay(ABC):
    def sendinfo(self):
        print("You can enter their mobile number or scanner")
    def amount(self):
        print("You can enter amount")
    def pin(self):
        print("You need to enter the pin")
    @abstractmethod
    def transaction(self):
        pass
class HDFC(Phonepay):
    def transaction(self):
        print("Payment using hdfc bank")        
class SBI(Phonepay):
    def transaction(self):
        print("Payment using sbi bank")        
class AXIS(Phonepay):
    def transaction(self):
        print("Payment using axis bank")        
class UNION(Phonepay):
    def transaction(self):
        print("Payment using union bank") 
class ICIC(Phonepay):
    def transaction(self):
        print("Payment using icic bank")
Anjana=HDFC()
Anjana.transaction()
Anjana.sendinfo() 
Anjana.amount()
Anjana.pin()
Amani=SBI()
Amani.transaction() 
Amani.sendinfo() 
Amani.amount()
Amani.pin()
Sri=UNION()
Sri.transaction()
Sri.sendinfo() 
Sri.amount()
Sri.pin() 
Reena=AXIS()
Reena.transaction()
Reena.sendinfo() 
Reena.amount()
Reena.pin()                                                      