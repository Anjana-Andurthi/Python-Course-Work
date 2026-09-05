class whatsappV1:
    def __init__(self,name):
        self.name=name
        print(f"welcome to the whatsapp - V1 {self.name}!")
    def messaging(self):
        print("You can send messages")

class whatsappV2(whatsappV1):
    def __init__(self,name):
        self.name=name
        print(f"welcome to the whatsapp - V2 {self.name}!")
    def calls(self):
        print("You can do audio and video calls") 

Anjana = whatsappV1('Anjana')
Anjana.messaging()

Amani = whatsappV2('Amani')
Amani.messaging()
Amani.calls()