class Hotstar:
    def __init__(self,name):
        print(f"Welcome to the Hotstar,{name}")
    def login(self):
        print("You can login to the Hotstar")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can search")
    def playcontrollers(self):
        print("pause.resume.play")
    def history(self):
        print("You can see the recent history")
    def ads(self):
        print("Ads will run")
    def quality(self):
        print("you can see with low quality")    
    def access(self):
        print("you can have limited access")                                                
    def download(self):
        print("You can download with low quality") 

class PremiumHotstar(Hotstar):
    def __init__(self,name):
        print(f"Welcome to the Hotstar,{name}")
    def ads(self):
        print("Ads will not run")
    def quality(self):
        print("you can see with high quality")    
    def access(self):
        print("you can have unlimited access")                                                
    def download(self):
        print("You can download with high quality") 

Anjana=Hotstar("Anjana")
Anjana.login()
Anjana.dashboard()
Anjana.search()
Anjana.playcontrollers()
Anjana.history()
Anjana.ads()
Anjana.quality()
Anjana.access()
Anjana.download()

Amani=PremiumHotstar("Amani")
Amani.login()
Amani.dashboard()
Amani.search()
Amani.playcontrollers()
Amani.history()
Amani.ads()
Amani.quality()
Amani.access()
Amani.download()
