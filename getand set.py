class Test:
    def setName(self,name):
        self.name=name
    def getName(self):
        return(self,self.name)
    
t=Test()
t.setName("ITM")
print("Your name :",t.getName())