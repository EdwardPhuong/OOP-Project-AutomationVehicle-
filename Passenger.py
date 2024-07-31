import Animal
import Human
import random
import openpyxl


#Passenger Class
class Passenger:
    def __init__(self):
        self.type = ""
        self.isDead = False
        self.passenger = None

    def __str__(self):
        return f"Type: {self.type}\nIs Dead: {self.isDead} \nPassenger: {self.passenger}"
    
    def getPassenger(self):
        passengerTypes=["Human", "Animal"]
        passengerSelector = random.choice(passengerTypes)
        if str(passengerSelector) == "Human":
            self.type = "Human"
            human = Human.Human()
            passenger = human.getHuman()
            self.passenger = passenger
        elif str(passengerSelector) == "Animal":
            self.type = "Animal"
            animal = Animal.Animal()
            passenger = animal.getAnimal()
            self.passenger = passenger
        return self

if __name__ == "__main__":
    mypassenger = Passenger()
    print(mypassenger.getPassenger())
    