class whatsappV1:
    def status(self):
        print("you can add images and videos")
class whatsappV2:
    def status(self):
        print("You can add music and stickers")

class whatsappV3(whatsappV1,whatsappV2):
    def status(self):
        whatsappV1.status()
        whatsappV2.status()

        print("You can like and you can react to the status")

c=whatsappV3()
c.status()
