import random
import openpyxl
import Passenger


#Vehicle Class
class Vehicle:
    def __init__(self):
        self.name = ""
        self.type = ""
        self.numberOfseat = 0
        self.passengers = []
        self.passengersString = ""
        self.isCrashed = False
        self.totalPriority = 0
        self.numberOfPassengers = 0

    def __str__(self):
        return f"\n-Vehicle- \nName: {self.name}\nType: {self.type}\nNumber of Seat: {self.numberOfseat}\nIs Crashed: {self.isCrashed} \nTotal Passengers: {self.numberOfPassengers}\nPassengers: {self.passengersString}\nTotal Priority: {self.totalPriority}"

    def getVehicleName(self):
        try:
            myVehicleNames = []
            workbook = openpyxl.load_workbook('resources/vehicles.xlsx')
            sheet = workbook['Sheet1']

            #Get All Vehicles' Name
            for col in sheet.columns:
                if str(col[0].value) == "Name":
                    for name in col[1:]:
                        if name.value != None: #Except None
                            myVehicleNames.append(name.value) #Add Vehicle to List
            self.name = random.choice(myVehicleNames) #Get Random Vehicle
            workbook.close()
            return self
        except Exception as e:
            print(e)
    
    def getVehicle(self):
        try:
            self.getVehicleName()
            workbook = openpyxl.load_workbook('resources/vehicles.xlsx')
            sheet = workbook['Sheet1']
            
            for col in sheet.columns:
                if str(col[0].value) == "Name":
                    for name in col[1:]:
                        if name.value == self.name: #Find Vehicle
                            self.type = name.offset(0, 1).value #Get Vehicle Type
                            self.numberOfseat = int(name.offset(0, 2).value) #Get Number of Seat
                            workbook.close()
                            return self
        except Exception as e:
            print(e)
    
    def loadPassenger(self):
        try:
            for i in range(0, self.numberOfseat):
                passenger = Passenger.Passenger()
                passenger.getPassenger()
                self.passengers.append(passenger)
                self.numberOfPassengers += 1
            return self.numberOfPassengers
        except Exception as e:
            print(e)
    
    def getPassengers(self):
        try:
            passengersString = ""
            passengers = self.passengers
            for passenger in passengers:
                if passenger.type != "Animal":
                    passengerCareer = passenger.passenger.career
                    if passengerCareer != "Executive":
                        passengersString += str(passengerCareer[0])
                    else:
                        passengersString += str(passengerCareer[0] + passengerCareer[1])
            self.passengersString = passengersString
            return self.passengersString, self.passengers
        except Exception as e:
            print(f"Error: {e}")

    def getTotalPriority(self):
        try:
            totalPriority = 0
            for passenger in self.passengers:
                priority = passenger.passenger.priority
                totalPriority += priority
            self.totalPriority = totalPriority
            return self.totalPriority
        except Exception as e:
            print(e)

if __name__ == "__main__":
    myVehicle = Vehicle()
    myVehicle.getVehicle()
    passengers = myVehicle.loadPassenger()
    myVehicle.getTotalPriority()
    myVehicle.getPassengers()
    print(myVehicle)
    # for passenger in passengers:
    #     print(passenger.passenger)