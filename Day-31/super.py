class whatsappV1:
    def status(self):
        print("you can add images and videos")
class whatsappV2(whatsappV1):
    def status(self):
        super().status()
        print("You can add music and stickers")
class whatsappV3(whatsappV2):
    def status(self):
        super().status()
        print("You can like and you can react to the status")

c=whatsappV3()
c.status()
