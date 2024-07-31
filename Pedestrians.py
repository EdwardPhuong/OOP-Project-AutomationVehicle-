import Animal
import Human
import random
import openpyxl


#Pedestrians Class
class Pedestrians:
    def __init__(self):
        self.type = ""
        self.isDead = False
        self.pedestrians = None

    def __str__(self):
        return f"Type: {self.type}\nIs Dead: {self.isDead} \nPedestrian: {self.pedestrians}"
    
    def getPedestrians(self):
        pedestriansTypes=["Human", "Animal"]
        pedestriansSelector = random.choice(pedestriansTypes)
        if str(pedestriansSelector) == "Human":
            self.type = "Human"
            human = Human.Human()
            pedestrians = human.getHuman()
            self.pedestrians = pedestrians
        elif str(pedestriansSelector) == "Animal":
            self.type = "Animal"
            animal = Animal.Animal()
            pedestrians = animal.getAnimal()
            self.pedestrians = pedestrians
        return self

if __name__ == "__main__":
    myPedestrians = Pedestrians()
    print(myPedestrians.getPedestrians())
    