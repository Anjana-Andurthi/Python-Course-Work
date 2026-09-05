class whatsappV1:
    def messaging(self):
        print("you can message")
class whatsappV2:
    def extramessages(self):
        print("You can add emojis,stickers,gifs")

class whatsappV3(whatsappV1,whatsappV2):
    def calls(self):
        print("You can do audio and video calls")
class whatsappV4(whatsappV3):
    def status(self):
        print("You can add status and see it for 24hrs")
a=whatsappV1()
a.messaging()

b=whatsappV2()
b.extramessages()

c=whatsappV3()
c.messaging()
c.extramessages()
c.calls()

d=whatsappV4()
d.messaging()
d.extramessages()
d.calls()
d.status()