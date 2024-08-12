import random
import Vehicle
import Pedestrians
import openpyxl
from openpyxl.utils import get_column_letter
'''
Priority:
1: Saving More Lives
2: Gender Preference (Male, Female, Other)
3: Social Value Preference 
4: Age Preference (Young, Adult, Elder)
==> Priority Table: resources/humans.xlsx
'''
#Driver
class MoralMachine:
    def __init__(self):
        self.isPedestriansCrossing = False
        self.numberOfcrossingPerdestrians = 0
        self.listOfcossingPedestrians = []

        self.pedestriansString = ""
        self.scenario = ""

        self.totalPriority = 0

        self.numberOfHumansDeath = 0
        self.numberOfHumansAlive = 0

        self.numberOfAnimalsDeath = 0
        self.numberOfAnimalsAlive = 0

        self.numberOfHumanPedestrians = 0
        self.numberOfAnimalPedestrians = 0

        self.totalNumberOfHumans = 0
        self.totalNumberOfAnimals = 0

        self.humansDeath = {}
        self.animalsDeath = {}

        self.result = []
    def __str__(self):
        return f"\nResult: {self.result}"

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
            numberOfHumanPedestrians = 0
            numberOfAnimalPedestrians = 0

            listOfcossingPedestrians = []
            for i in range(0, numberOfPedestrians):
                pedestrian = Pedestrians.Pedestrians()
                pedestrian.getPedestrians()
                if pedestrian.type == "Human":
                    numberOfHumanPedestrians += 1
                else:
                    numberOfAnimalPedestrians += 1
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
            self.numberOfHumanPedestrians = numberOfHumanPedestrians
            self.numberOfAnimalPedestrians = numberOfAnimalPedestrians
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
            totalNumberOfHumans = 0
            totalNumberOfAnimals = 0
            
            numberOfHumansDeath = 0
            numberOfHumansAlive = 0

            numberOfAnimalsDeath = 0
            numberOfAnimalsAlive = 0

            humanTypes = self.humansDeath
            animalTypes = self.animalsDeath

            if pedestrians is not None:
                for pedestrian in pedestrians[1]:
                    if pedestrian.type == "Human":
                        totalNumberOfHumans += 1
                    else:
                        totalNumberOfAnimals += 1
                        
            if passengers is not None:
                for passenger in passengers[1]:
                    if passenger.type == "Human":
                        totalNumberOfHumans += 1
                    else:
                        totalNumberOfAnimals += 1

            if otherPedestrians is not None:
                for pedestrian in otherPedestrians[1]:
                    if pedestrian.type == "Human":
                        totalNumberOfHumans += 1
                    else:
                        totalNumberOfAnimals += 1

            self.totalNumberOfHumans += totalNumberOfHumans
            self.totalNumberOfAnimals += totalNumberOfAnimals
            print("Total Number of Humans: " + str(self.totalNumberOfHumans) + "\nTotal Number of Animals: " + str(self.totalNumberOfAnimals))
            if str(scenario[0]) == "0":
                print("\n------------------DECISIONS---------------------\n")
                print("Saving More Lives \nSaving More Values People \nSaving More Female \nSaving Young Generation")
                myPedestrians = pedestrians[1]
                totalPedestriansPriority = self.getTotalPriority("Pedestrians", myPedestrians)
                myPassengers = passengers[1]
                totalPassengersPriority = self.getTotalPriority("Passengers", myPassengers)
                myOtherPedestrians = otherPedestrians[1]
                totalOtherPedestriansPriority = self.getTotalPriority("Pedestrians", myOtherPedestrians)

                # 0 = No Legal Complication
                # 1 = Legal Complication (CURRENT LANE IS GREEN OTHER IS RED)
                # 2 = Legal Complication (CURRENT LANE IS RED OTHER IS GREEN)
                #NOTICE -> NO PRIOTIY FOR UPHOLDING THE LAW.
                # ==> COMBINE 3 SCENARIOS (NO LEGAL COMPLICATION)
                if str(scenario[1]) == "0" or str(scenario[1]) == "1" or str(scenario[1]) == "2": 
                    if  totalPedestriansPriority > totalOtherPedestriansPriority:
                        print("Pedestrians > Other Pedestrians")
                        for pedestrian in myOtherPedestrians:
                            pedestrian.isDead = True
                            if pedestrian.type == "Human":
                                numberOfHumansDeath += 1
                                human = pedestrian.pedestrian.career
                                humanTypes[human] = humanTypes.get(human, 0) + 1
                            else:
                                numberOfAnimalsDeath += 1
                                animal = pedestrian.pedestrian.species
                                animalTypes[animal] = animalTypes.get(animal, 0) + 1

                        self.humansDeath = humanTypes
                        self.animalsDeath = animalTypes
                        self.numberOfHumansDeath += numberOfHumansDeath
                        self.numberOfAnimalsDeath += numberOfAnimalsDeath

                        for passenger in myPassengers:
                            if passenger.type == "Human":
                                numberOfHumansAlive += 1
                            else:
                                numberOfAnimalsAlive += 1
                        for pedestrian in myPedestrians:
                            if pedestrian.type == "Human":
                                numberOfHumansAlive += 1
                            else:
                                numberOfAnimalsAlive += 1

                        self.numberOfHumansAlive += numberOfHumansAlive
                        self.numberOfAnimalsAlive += numberOfAnimalsAlive
                        print("\n----------------------SUMMARY---------------------\n")
                        print(f"Passengers: {passengers[0]}")
                        print(f"Total Passenger Priority: {totalPassengersPriority}")
                        print(f"Pedestrians: {pedestrians[0]}")
                        print(f"Total Pedestrian Priority: {totalPedestriansPriority}")
                        print(f"Other Pedestrians: {otherPedestrians[0]}")
                        print(f"Total Other Pedestrian Priority: {totalOtherPedestriansPriority}")
                        print("\n----------------------SUMMARY---------------------\n")
                        return True
                    
                    else:
                        print("Other Pedestrians > Pedestrians")
                        for pedestrian in myPedestrians:
                            pedestrian.isDead = True
                            if pedestrian.type == "Human":
                                numberOfHumansDeath += 1
                                human = pedestrian.pedestrian.career
                                humanTypes[human] = humanTypes.get(human, 0) + 1
                            else:
                                numberOfAnimalsDeath += 1
                                animal = pedestrian.pedestrian.species
                                animalTypes[animal] = animalTypes.get(animal, 0) + 1

                        self.humansDeath = humanTypes
                        self.animalsDeath = animalTypes
                        self.numberOfHumansDeath += numberOfHumansDeath
                        self.numberOfAnimalsDeath += numberOfAnimalsDeath

                        for passenger in myPassengers:
                            if passenger.type == "Human":
                                numberOfHumansAlive += 1
                            else:
                                numberOfAnimalsAlive += 1
                        for pedestrian in myOtherPedestrians:
                            if pedestrian.type == "Human":
                                numberOfHumansAlive += 1
                            else:
                                numberOfAnimalsAlive += 1
                                
                        self.numberOfHumansAlive += numberOfHumansAlive
                        self.numberOfAnimalsAlive += numberOfAnimalsAlive

                        print("\n----------------------SUMMARY---------------------\n")
                        print(f"Passengers: {passengers[0]}")
                        print(f"Total Passenger Priority: {totalPassengersPriority}")
                        print(f"Pedestrians: {pedestrians[0]}")
                        print(f"Total Pedestrian Priority: {totalPedestriansPriority}")
                        print(f"Other Pedestrians: {otherPedestrians[0]}")
                        print(f"Total Other Pedestrian Priority: {totalOtherPedestriansPriority}")
                        print("\n----------------------SUMMARY---------------------\n")
                        return False
            
            # choose to stay in the lane and hit one group of pedestrians or sway
            # into the other lane and hit a concrete barricade kill all passengers,
            elif str(scenario[0]) == "1":
                print("\n------------------DECISIONS---------------------\n")
                print("Saving More Lives \nSaving More Values People \nSaving More Female \nSaving Young Generation")
                print("\n------------------DECISIONS---------------------\n")
                myPedestrians = pedestrians[1]
                totalPedestriansPriority = self.getTotalPriority("Pedestrians", myPedestrians)
                myPassengers = passengers[1]
                totalPassengersPriority = self.getTotalPriority("Passengers", myPassengers)

                # 0 = No Legal Complication
                # 1 = Legal Complication (CURRENT LANE IS GREEN OTHER IS RED)
                # 2 = Legal Complication (CURRENT LANE IS RED OTHER IS GREEN)
                #NOTICE -> NO PRIOTIY FOR UPHOLDING THE LAW.
                # ==> COMBINE 3 SCENARIOS (NO LEGAL COMPLICATION)
                if str(scenario[1]) == "0" or str(scenario[1]) == "1" or str(scenario[1]) == "2":
                    if totalPassengersPriority > totalPedestriansPriority:
                        print("Passengers > Pedestrians")
                        for pedestrian in myPedestrians:
                            pedestrian.isDead = True
                            if pedestrian.type == "Human":
                                numberOfHumansDeath += 1
                                human = pedestrian.pedestrian.career
                                humanTypes[human] = humanTypes.get(human, 0) + 1
                            else:
                                numberOfAnimalsDeath += 1
                                animal = pedestrian.pedestrian.species
                                animalTypes[animal] = animalTypes.get(animal, 0) + 1

                        self.humansDeath = humanTypes
                        self.animalsDeath = animalTypes
                        self.numberOfHumansDeath += numberOfHumansDeath
                        self.numberOfAnimalsDeath += numberOfAnimalsDeath

                        for passenger in myPassengers:
                            if passenger.type == "Human":
                                numberOfHumansAlive += 1
                            else:
                                numberOfAnimalsAlive += 1

                        self.numberOfHumansAlive += numberOfHumansAlive
                        self.numberOfAnimalsAlive += numberOfAnimalsAlive
                        print("\n----------------------SUMMARY---------------------\n")
                        print(f"Passengers: {passengers[0]}")
                        print(f"Total Passenger Priority: {totalPassengersPriority}")
                        print(f"Pedestrians: {pedestrians[0]}")
                        print(f"Total Pedestrian Priority: {totalPedestriansPriority}")
                        print("\n----------------------SUMMARY---------------------\n")
                        return False

                    else:
                        print("Pedestrians > Passengers")
                        for passenger in myPassengers:
                            passenger.isDead = True
                            if passenger.type == "Human":
                                numberOfHumansDeath += 1
                                human = passenger.passenger.career
                                humanTypes[human] = humanTypes.get(human, 0) + 1
                            else:
                                numberOfAnimalsDeath += 1
                                animal = passenger.passenger.species
                                animalTypes[animal] = animalTypes.get(animal, 0) + 1

                        self.humansDeath = humanTypes
                        self.animalsDeath = animalTypes
                        self.numberOfHumansDeath += numberOfHumansDeath
                        self.numberOfAnimalsDeath += numberOfAnimalsDeath

                        for pedestrian in myPedestrians:
                            if pedestrian.type == "Human":
                                numberOfHumansAlive += 1
                            else:
                                numberOfAnimalsAlive += 1

                        self.numberOfHumansAlive += numberOfHumansAlive
                        self.numberOfAnimalsAlive += numberOfAnimalsAlive
                        print("\n----------------------SUMMARY---------------------\n")
                        print(f"Pedestrians: {pedestrians[0]}")
                        print(f"Total Pedestrian Priority: {totalPedestriansPriority}")
                        print(f"Passengers: {passengers[0]}")
                        print(f"Total Passenger Priority: {totalPassengersPriority}")
                        print("\n----------------------SUMMARY---------------------\n")
                        return True
                                
            # choose to stay in the lane and hit a concrete barricade that will kill
            # the group of passengers inside the vehicle or sway to hit concrete barricades.
            elif str(scenario[0]) == "2":
                print("\n------------------DECISIONS---------------------\n")
                print("Saving More Values People \nSaving More Lives \nSaving More Female \nSaving Young Generation")
                print("\n------------------DECISIONS---------------------\n")
                myPedestrians = pedestrians[1]
                totalPedestriansPriority = self.getTotalPriority("Pedestrians", myPedestrians)
                myPassengers = passengers[1]
                totalPassengersPriority = self.getTotalPriority("Passengers", myPassengers)
                
                # 0 = No Legal Complication
                # 1 = Legal Complication (CURRENT LANE IS GREEN OTHER IS RED)
                # 2 = Legal Complication (CURRENT LANE IS RED OTHER IS GREEN)
                #NOTICE -> NO PRIOTIY FOR UPHOLDING THE LAW.
                # ==> COMBINE 3 SCENARIOS (NO LEGAL COMPLICATION)
                if str(scenario[1]) == "0" or str(scenario[1]) == "1" or str(scenario[1]) == "2":
                    if totalPassengersPriority > totalPedestriansPriority:
                        print("Passengers > Pedestrians")
                        for pedestrian in myPedestrians:
                            pedestrian.isDead = True
                            if pedestrian.type == "Human":
                                numberOfHumansDeath += 1
                                human = pedestrian.pedestrian.career
                                humanTypes[human] = humanTypes.get(human, 0) + 1
                            else:
                                numberOfAnimalsDeath += 1
                                animal = pedestrian.pedestrian.species
                                animalTypes[animal] = animalTypes.get(animal, 0) + 1

                        self.humansDeath = humanTypes
                        self.animalsDeath = animalTypes
                        self.numberOfHumansDeath += numberOfHumansDeath
                        self.numberOfAnimalsDeath += numberOfAnimalsDeath

                        for passenger in myPassengers:
                            if passenger.type == "Human":
                                numberOfHumansAlive += 1
                            else:
                                numberOfAnimalsAlive += 1

                        self.numberOfHumansAlive += numberOfHumansAlive
                        self.numberOfAnimalsAlive += numberOfAnimalsAlive
                        print("\n----------------------SUMMARY---------------------\n")
                        print(f"Passengers: {passengers[0]}")
                        print(f"Total Passenger Priority: {totalPassengersPriority}")
                        print(f"Pedestrians: {pedestrians[0]}")
                        print(f"Total Pedestrian Priority: {totalPedestriansPriority}")
                        print("\n----------------------SUMMARY---------------------\n")
                        return True
                    
                    else:
                        print("Pedestrians > Passengers")
                        for passenger in myPassengers:
                            passenger.isDead = True
                            if passenger.type == "Human":
                                numberOfHumansDeath += 1
                                human = passenger.passenger.career
                                humanTypes[human] = humanTypes.get(human, 0) + 1
                            else:
                                numberOfAnimalsDeath += 1
                                animal = passenger.passenger.species
                                animalTypes[animal] = animalTypes.get(animal, 0) + 1

                        self.humansDeath = humanTypes
                        self.animalsDeath = animalTypes
                        self.numberOfHumansDeath += numberOfHumansDeath
                        self.numberOfAnimalsDeath += numberOfAnimalsDeath

                        for pedestrian in myPedestrians:
                            if pedestrian.type == "Human":
                                numberOfHumansAlive += 1
                            else:
                                numberOfAnimalsAlive += 1

                        self.numberOfHumansAlive += numberOfHumansAlive
                        self.numberOfAnimalsAlive += numberOfAnimalsAlive
                        print("\n----------------------SUMMARY---------------------\n")
                        print(f"Pedestrians: {pedestrians[0]}")
                        print(f"Total Pedestrian Priority: {totalPedestriansPriority}")
                        print(f"Passengers: {passengers[0]}")
                        print(f"Total Passenger Priority: {totalPassengersPriority}")
                        print("\n----------------------SUMMARY---------------------\n")
                        return False

        except Exception as e:
            print(f"Error: {e}")
    
    def testAlgorithm(self, numberOfScenarios):
        try:
            print("\n----------------------Test Algorithm Function---------------------\n")
            print("Priorities: \n1: Saving More Lives \n2: Gender Preference \n3: Social Value Preference \n4: Gender Preference")
            result = []
            humanTypes = {}
            animalTypes = {}

            for i in range(0, numberOfScenarios):
                scenario = self.getScenario()
                print(f"\nScenario: {scenario}")
                if scenario[0] != "0":
                    myVehicle = Vehicle.Vehicle()
                    myVehicle.getVehicle()
                    numberOfPassengers = myVehicle.loadPassenger()

                    passengers = myVehicle.getPassengers()
                    pedestrians = self.getPedestrian(numberOfPassengers)

                    if passengers is not None:
                        for passenger in passengers[1]:
                            if passenger.type == "Human":
                                human = passenger.passenger.career
                                humanTypes[human] = humanTypes.get(human, 0) + 1
                            else:
                                animal = passenger.passenger.species
                                animalTypes[animal] = animalTypes.get(animal, 0) + 1
                    if pedestrians is not None:
                        for pedestrian in pedestrians[1]:
                            if pedestrian.type == "Human":
                                human = pedestrian.pedestrian.career
                                humanTypes[human] = humanTypes.get(human, 0) + 1
                            else:
                                animal = pedestrian.pedestrian.species
                                animalTypes[animal] = animalTypes.get(animal, 0) + 1
                    
                    self.decideSwerve(scenario, pedestrians, passengers)
                else:
                    myVehicle = Vehicle.Vehicle()
                    myVehicle.getVehicle()
                    numberOfPassengers = myVehicle.loadPassenger()

                    passengers = myVehicle.getPassengers()
                    pedestrians = self.getPedestrian(numberOfPassengers)
                    otherPedestrians = self.getPedestrian(numberOfPassengers)

                    if passengers is not None:
                        for passenger in passengers[1]:
                            if passenger.type == "Human":
                                human = passenger.passenger.career
                                humanTypes[human] = humanTypes.get(human, 0) + 1
                            else:
                                animal = passenger.passenger.species
                                animalTypes[animal] = animalTypes.get(animal, 0) + 1
                    if pedestrians is not None:
                        for pedestrian in pedestrians[1]:
                            if pedestrian.type == "Human":
                                human = pedestrian.pedestrian.career
                                humanTypes[human] = humanTypes.get(human, 0) + 1
                            else:
                                animal = pedestrian.pedestrian.species
                                animalTypes[animal] = animalTypes.get(animal, 0) + 1
                    if otherPedestrians is not None:
                        for pedestrian in otherPedestrians[1]:
                            if pedestrian.type == "Human":
                                human = pedestrian.pedestrian.career
                                humanTypes[human] = humanTypes.get(human, 0) + 1
                            else:
                                animal = pedestrian.pedestrian.species
                                animalTypes[animal] = animalTypes.get(animal, 0) + 1

                    self.decideSwerve(scenario, pedestrians, passengers, otherPedestrians)
            
            print("\n------------------------------SUMMARY---------------------------------\n")
            print(f"Total Number Humans: {self.totalNumberOfHumans}")
            print(f"Total Number Animals: {self.totalNumberOfAnimals}")
            print(f"Number of Dead Humans: {self.numberOfHumansDeath}")
            print(f"Number of Alive Humans: {self.numberOfHumansAlive}")
            print(f"Number of Dead Animals: {self.numberOfAnimalsDeath}")
            print(f"Number of Alive Animal: {self.numberOfAnimalsAlive}")
            print(f"Number of Human Pedestrians: {self.numberOfHumanPedestrians}")
            print(f"Number of Animal Pedestrians: {self.numberOfAnimalPedestrians}")
            print(f"Humans: {humanTypes}")
            print(f"Animals: {animalTypes}")            
            print(f"Dead Humans: {self.humansDeath}")
            print(f"Dead Animals: {self.animalsDeath}")
            print("\n------------------------------SUMMARY---------------------------------\n")
        except Exception as e:
            print(f"Error: {e}")

myRoad = MoralMachine()

test = myRoad.testAlgorithm(10)
