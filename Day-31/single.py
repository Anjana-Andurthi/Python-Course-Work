#single inheritance
class whatsappV1:
    def messaging(self):
        print("you can message")
class whatsappV2(whatsappV1):
    def calls(self):
        print("You can do audio and video calls")

a=whatsappV1()
a.messaging()

b=whatsappV2()
b.messaging()
b.calls()

