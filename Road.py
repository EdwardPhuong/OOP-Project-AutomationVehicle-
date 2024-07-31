import random
import Vehicle
import Pedestrians
#Driver
class Road:
    def __init__(self):
        self.isPedestriansCrossing = False
        self.numberOfcrossingPerdestrians = 0
        self.cossingPedestrians = []
        self.numberOfdeath = 0
        self.numberOfalive = 0
    def __str__(self):
        return f"Is Pedestrians Cross: {self.isPedestriansCrossing}\nNumber of crossing Pedestrians: {self.numberOfcrossingPerdestrians}\nNumber of death: {self.numberOfdeath}\nNumber of alive: {self.numberOfalive}"
    
    def getScenario(self):
        try:
            numberOfpedestrians = random.randint(4, 31)
            isCrossing = True
            for pedestrian in range(numberOfpedestrians):
                pedestrian = Pedestrians.Pedestrians()
                pedestrian.getPedestrians()
                self.cossingPedestrians.append(pedestrian)
            self.isPedestriansCrossing = isCrossing
            self.numberOfcrossingPerdestrians = numberOfpedestrians
            return self
        except Exception as e:
            print(f"Error: {e}")

    def run(self):
        try:
            myVehicle = Vehicle.Vehicle()
            myVehicle.getVehicle()
            myPassengers = myVehicle.loadPassenger()
            self.getScenario()
            if self.isPedestriansCrossing:
                if self.numberOfcrossingPerdestrians > myVehicle.numberOfseat:
                    myVehicle.isCrashed = True
                    for i in myPassengers:
                        i.isDead = True
                        print(i)
                    numberOfdeath = myVehicle.numberOfseat
                    numberOfalive = self.numberOfcrossingPerdestrians
                    self.numberOfdeath = numberOfdeath
                    self.numberOfalive = numberOfalive
                else:
                    myVehicle.isCrashed = False
                    for i in self.cossingPedestrians:
                        i.isDead = True
                        print(i)
                    numberOfdeath = self.numberOfcrossingPerdestrians
                    numberOfalive = myVehicle.numberOfseat
                    self.numberOfdeath = numberOfdeath
                    self.numberOfalive = numberOfalive
            print(myVehicle)
            print(self)
        except Exception as e:
            print(f"Error: {e}")

myRoad = Road()
myRoad.run()
# myRoad.getScenario()
# for predestrian in myRoad.cossingPedestrians:
#     print(predestrian)
# print(myRoad)
