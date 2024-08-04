import Animal
import Human
import random
import openpyxl


#pedestrian Class
class Pedestrians:
    def __init__(self):
        self.type = ""
        self.isDead = False
        self.pedestrian = None

    def __str__(self):
        return f"Type: {self.type}\nIs Dead: {self.isDead} \nPedestrian: {self.pedestrian}"
    
    def getPedestrians(self):
        pedestrianTypes=["Human", "Animal"]
        pedestrianSelector = random.choice(pedestrianTypes)
        if str(pedestrianSelector) == "Human":
            self.type = "Human"
            human = Human.Human()
            pedestrian = human.getHuman()
            self.pedestrian = pedestrian
        elif str(pedestrianSelector) == "Animal":
            self.type = "Animal"
            animal = Animal.Animal()
            pedestrian = animal.getAnimal()
            self.pedestrian = pedestrian
        return self

if __name__ == "__main__":
    mypedestrian = Pedestrians()
    print(mypedestrian.getPedestrians())
    