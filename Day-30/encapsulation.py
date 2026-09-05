class Instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self._posts=[]

    def getpassword(self):
        return self.__password
    def setpassword(self,newpassword):
        self.__password=newpassword    

    @property
    def accesspost(self):
        return self._posts

    @accesspost.setter  #to update the protected class
    def accesspost(self,newpost):
        self._posts.append(newpost)


    def display(self):
        print(self.username,self.__password,self._posts) 

Anjana = Instagram('Anjana','anjana@123')
Anjana.display()
print(Anjana.username)
print(Anjana.getpassword())
print(Anjana.accesspost)     

Anjana.username='Amani'
Anjana.setpassword('amani@123')
Anjana.accesspost="Sunrise.png"
Anjana.accesspost="Beach.png"
Anjana.accesspost="Temple.png"
print(Anjana.username)
print(Anjana.getpassword())
print(Anjana.accesspost)
