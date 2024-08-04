import random
import Vehicle
import Pedestrians
import openpyxl
from openpyxl.utils import get_column_letter
#Driver
class MoralMachine:
    def __init__(self):
        self.isPedestriansCrossing = False
        self.numberOfcrossingPerdestrians = 0
        self.listOfcossingPedestrians = []

        self.pedestriansString = ""
        self.scenario = ""

        self.numberOfdeath = 0
        self.numberOfalive = 0
        self.totalPriority = 0

    def __str__(self):
        return f"\nScenario: {self.scenario}\nIs Pedestrians Cross: {self.isPedestriansCrossing}\nPedestrians: {self.pedestriansString}\nNumber of crossing Pedestrians: {self.numberOfcrossingPerdestrians}\nTotal Priority: {self.totalPriority}\nNumber of death: {self.numberOfdeath}\nNumber of alive: {self.numberOfalive}"

    def getScenario(self):
        try:
            scenarios = random.choice([0,1,2])
            legalComplicationPresent = random.choice([0,1,2])
            scenario = "".join([str(scenarios), str(legalComplicationPresent)])
            self.scenario = scenario
            return self.scenario
        except Exception as e:
            print(f"Error: {e}")

    def getPedestrian(self, numberOfPassengers):
        try:
            numberOfPedestrians = numberOfPassengers #Get Number of Pedestrians = Number of Passengers (#Default = 5)
            pedestriansString = ""
            numberOfCrossingPedestrians = 0
            listOfcossingPedestrians = []
            for i in range(0, numberOfPedestrians):
                pedestrian = Pedestrians.Pedestrians()
                pedestrian.getPedestrians()
                listOfcossingPedestrians.append(pedestrian)
                numberOfCrossingPedestrians += 1
            for pedestrian in listOfcossingPedestrians:
                if pedestrian.type != "Animal":
                    pedestrianCareer = pedestrian.pedestrian.career
                    if pedestrianCareer != "Executive":
                        pedestriansString += str(pedestrianCareer[0])
                    else:
                        pedestriansString += str(pedestrianCareer[0] + pedestrianCareer[1])
            self.listOfcossingPedestrians = listOfcossingPedestrians
            self.pedestriansString = pedestriansString
            self.numberOfcrossingPerdestrians = numberOfCrossingPedestrians
            return self.pedestriansString, self.listOfcossingPedestrians, self.numberOfcrossingPerdestrians
        except Exception as e:
            print(f"Error: {e}")
    
    def getTotalPriority(self, type, list):
        try:
            if type == "Pedestrians":
                totalPriority = 0
                listOfTargets = list
                for target in listOfTargets:
                    priority = target.pedestrian.priority
                    totalPriority += priority
                self.totalPriority = totalPriority
                return self.totalPriority
            else:
                totalPriority = 0
                listOfTargets = list
                for target in listOfTargets:
                    priority = target.passenger.priority
                    totalPriority += priority
                self.totalPriority = totalPriority
                return self.totalPriority
        except Exception as e:
            print(f"Error: {e}")
    
    def decideSwerve(self, scenario, pedestrians, passengers, otherPedestrians = None):
        try:
            """
            choose to stay in the lane and hit one group of pedestrians or sway
            into the other lane and hit a different group of pedestrians
            """
            if str(scenario[0]) == "0":
                myPedestrians = pedestrians[1]
                totalPedestriansPriority = self.getTotalPriority("Pedestrians", myPedestrians)
                myPassengers = passengers[1]
                totalPassengersPriority = self.getTotalPriority("Passengers", myPassengers)
                myOtherPedestrians = otherPedestrians[1]
                totalOtherPedestriansPriority = self.getTotalPriority("Pedestrians", myOtherPedestrians)

                if str(scenario[1]) == "0": #No Legal Complication
                    print(f"Total Passengers Priority: {totalPassengersPriority}")
                    print(f"Total Pedestrians Priority: {totalPedestriansPriority}")
                    print(f"Total Other Pedestrians Priority: {totalOtherPedestriansPriority}")
                    if  totalPedestriansPriority > totalOtherPedestriansPriority:
                        print("Pedestrians > Other Pedestrians")
                        if totalPassengersPriority > totalOtherPedestriansPriority:
                            print("Passengers > Other Pedestrians")
                            print("\n------------------DEAD---------------------\n")
                            for pedestrian in myOtherPedestrians:
                                pedestrian.isDead = True
                                print(pedestrian)
                            print("\n------------------DEAD---------------------n")
                            print("\n--------------------ALIVE---------------------\n")
                            for passenger in myPassengers:
                                print(passenger)
                            for pedestrian in myPedestrians:
                                print(pedestrian)
                            print("\n--------------------ALIVE---------------------n")
                            print("\n----------------------SUMMARY---------------------\n")
                            print(f"Passengers: {passengers[0]}")
                            print(f"Total Passenger Priority: {totalPassengersPriority}")
                            print(f"Pedestrians: {pedestrians[0]}")
                            print(f"Total Pedestrian Priority: {totalPedestriansPriority}")
                            print(f"Other Pedestrians: {otherPedestrians[0]}")
                            print(f"Total Other Pedestrian Priority: {totalOtherPedestriansPriority}")
                            print("\n----------------------SUMMARY---------------------\n")
                    else:
                        print("Other Pedestrians > Pedestrians")
                        if totalPassengersPriority > totalPedestriansPriority:
                            print("Passengers > Pedestrians")
                            print("\n------------------DEAD---------------------\n")
                            for pedestrian in myPedestrians:
                                pedestrian.isDead = True
                                print(pedestrian)
                            print("\n------------------DEAD---------------------n")
                            print("\n--------------------ALIVE---------------------\n")
                            for passenger in myPassengers:
                                print(passenger)
                            for pedestrian in myOtherPedestrians:
                                print(pedestrian)
                            print("\n--------------------ALIVE---------------------n")
                            print("\n----------------------SUMMARY---------------------\n")
                            print(f"Passengers: {passengers[0]}")
                            print(f"Total Passenger Priority: {totalPassengersPriority}")
                            print(f"Pedestrians: {pedestrians[0]}")
                            print(f"Total Pedestrian Priority: {totalPedestriansPriority}")
                            print(f"Other Pedestrians: {otherPedestrians[0]}")
                            print(f"Total Other Pedestrian Priority: {totalOtherPedestriansPriority}")
                            print("\n----------------------SUMMARY---------------------\n")
                    



        except Exception as e:
            print(f"Error: {e}")
    
    def testAlgorithm(self, numberOfScenarios):
        try:
            for i in range(0, numberOfScenarios):
                scenario = self.getScenario()
                print(f"\nScenario: {scenario[0]}")
                if scenario[0] != "0":
                    myVehicle = Vehicle.Vehicle()
                    myVehicle.getVehicle()
                    numberOfPassengers = myVehicle.loadPassenger()

                    passengers = myVehicle.getPassengers()
                    pedestrians = self.getPedestrian(numberOfPassengers)

                    self.decideSwerve(scenario, pedestrians, passengers)

                else:
                    myVehicle = Vehicle.Vehicle()
                    myVehicle.getVehicle()
                    numberOfPassengers = myVehicle.loadPassenger()

                    passengers = myVehicle.getPassengers()
                    pedestrians = self.getPedestrian(numberOfPassengers)
                    otherPedestrians = self.getPedestrian(numberOfPassengers)

                    self.decideSwerve(scenario, pedestrians, passengers, otherPedestrians)
        except Exception as e:
            print(f"Error: {e}")

myRoad = MoralMachine()
test = myRoad.testAlgorithm(10)
