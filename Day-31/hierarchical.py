class whatsappV1:
    def messaging(self):
        print("you can message")
class whatsappV2(whatsappV1):
    def calls(self):
        print("You can do audio and video calls")
class whatsappV3(whatsappV1):
    def status(self):
        print("You can add status and see it for 24hrs")
a=whatsappV1()
a.messaging()

b=whatsappV2()
b.messaging()
b.calls()

c=whatsappV3()
c.messaging()
c.status()