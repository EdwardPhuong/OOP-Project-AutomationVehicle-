import random
import openpyxl

#Animal Class
class Animal:
    def __init__(self):
        self.name = ""
        self.species = ""
        self.age = 0
        self.priority = 0
    
    def __str__(self):
        return f"\n-Animal- \nSpecies: {self.species}\nName: {self.name}\nAge: {self.age}\nPriority: {self.priority}"
    def getSpecies(self):
        try:
            mySpecies = []
            workbook = openpyxl.load_workbook('resources/animals.xlsx')
            sheet = workbook['Sheet1']

            #Get All Species
            for col in sheet.columns:
                if str(col[0].value) == "Species":
                    for species in col[1:]:
                        if species.value != None: #Except None
                            mySpecies.append(species.value) #Add Species to List
            self.species = random.choice(mySpecies) #Get Random Species
            workbook.close()
            return self.species
        except Exception as e:
            print(e)

    def getName(self):
        try:
            myNames = []
            workbook = openpyxl.load_workbook('resources/animals.xlsx')
            sheet = workbook['Sheet1']

            #Get All Names
            for col in sheet.columns:
                if str(col[0].value) == "Name":
                    for name in col[1:]:
                        if name.value != None: #Except None
                            myNames.append(name.value) #Add Name to List
            self.name = random.choice(myNames) #Get Random Name
            workbook.close()
            return self.name
        except Exception as e:
            print(e)
    
    def getAge(self):
        try:
            myAge = 0
            myAge = random.randint(1, 15)
            self.age = myAge
            return self.age
        except Exception as e:
            print(e)

    #Initalize Animal
    def getAnimal(self):
        self.getSpecies()
        self.getName()
        self.getAge()
        return self


if __name__ == "__main__":
    myanimal = Animal()
    print(myanimal.getAnimal())