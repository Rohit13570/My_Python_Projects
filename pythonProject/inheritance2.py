class computer:
    def __init__(self, motherboard, ram):
        self.motherboard = motherboard
        self.ram = ram

    def getdetail(self):
        self.motherboard = str(input("Enter the motherboard name"))
        self.ram = str(input("Enter the ram"))

    def printdetail(self):
        print(self.motherboard)
        print(self.ram)
class deskstop(computer):
    def __init__(self, os, screen):
        self.os = os
        self.screen = screen
    def getdetails(self):
        self.os = str(input("Enter the os name"))
        self.screen = str(input("Enter the screen "))

    def printdetails(self):
        print(self.os)
        print(self.screen)


class laptop(computer):
    def __init__(self, size, display):
        self.size = size
        self.display = display

    def getdetailss(self):
        self.size = str(input("Enter the size"))
        self.display = str(input("Enter the display name"))

    def printdetailss(self):
        print(self.size)
        print(self.display)
obj=deskstop('','')
obj.getdetails()
obj.printdetails()
obj1=laptop('','')
obj1.getdetailss()
obj1.printdetailss()
