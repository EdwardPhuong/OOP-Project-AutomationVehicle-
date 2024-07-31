import random
import openpyxl

#Human Class
class Human:
    def __init__(self):
        self.name = ""
        self.gender = ""
        self.age = 0
    
    def __str__(self):
        return f"Name: {self.name}\nGender: {self.gender}\nAge: {self.age}"

    def getName(self):
        try:
            myNames = []
            workbook = openpyxl.load_workbook('resources/humans.xlsx')
            sheet = workbook['Sheet1']

            #Get All Names
            for col in sheet.columns:
                if str(col[0].value) == "Name":
                    for name in col[1:]:
                        if name.value != None: #Except None
                            myNames.append(name.value) #Add Name to List
            self.name = random.choice(myNames) #Get Random Name
            return self.name
        except Exception as e:
            print(e)

    def getGender(self):
        try:
            myGenders = ["Male", "Female", "Other"]
            self.gender = random.choice(myGenders)
            return self.gender
        except Exception as e:
            print(e)

    def getAge(self):
        try:
            myAge = 0
            myAge = random.randint(1, 100)
            self.age = myAge
            return self.age
        except Exception as e:
            print(e)

    #Initalize Human
    def getHuman(self):
        self.getName()
        self.getGender()
        self.getAge()
        return self
    

if __name__ == "__main__":
    myhuman = Human()
    print(myhuman.getHuman())
