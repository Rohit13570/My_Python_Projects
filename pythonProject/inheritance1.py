class hospital:
     def __init__(self,admin,doc,sis,dep):
         self.admin = admin
         self.doc = doc
         self.sis = sis
         self.dep = dep


     def getdetails(self):
         self.admin = str(input("Enter the admin name"))
         self.doc = str(input("Enter the doctor name"))
         self.sis= str(input("Enter the sister name"))
         self.dep = str(input("Enter the department name"))

class department(hospital):
     def printdetails(self):
         print(self.admin)
         print(self.doc)
         print(self.sis)
         print(self.dep)


class patientdetails():
    def __init__(self, name, age,num, disease):
        self.name = name
        self.age = age
        self.num = num
        self.disease = disease

    def getdetailss(self):
        self.name = str(input("Enter the patient name"))
        self.age = int(input("Enter the patient age"))
        self.num = int(input("Enter the number"))
        self.disease = str(input("Enter the disease name"))

    def printdetailss(self):
        print(self.name)
        print(self.age)
        print(self.num)
        print(self.disease)

obj=department('','','','')
obj.getdetails()
obj.printdetails()
obj1=patientdetails('','','','')
obj1.getdetailss()
obj1.printdetailss()




