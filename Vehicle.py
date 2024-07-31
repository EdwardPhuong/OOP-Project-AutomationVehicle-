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
        self.isCrashed = False
    
    def __str__(self):
        return f"Name: {self.name}\nType: {self.type}\nNumber of Seat: {self.numberOfseat}\nIs Crashed: {self.isCrashed}"

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
            return self.passengers
        except Exception as e:
            print(e)

if __name__ == "__main__":
    myVehicle = Vehicle()
    myVehicle.getVehicle()
    passengers = myVehicle.loadPassenger()
    for passenger in passengers:
        print(passenger.passenger)
    print(myVehicle)