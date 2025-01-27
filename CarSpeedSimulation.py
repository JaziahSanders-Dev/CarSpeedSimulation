# ---------------------------------------------
# Name: Jaziah Sanders
# Project: Car Speed Simulation
# Class: COSC 1336
# ---------------------------------------------
# Project Objectives
#  Write a program that creates a Car object. It prompts the user for the car’s year and make, as
#  well as the number of times the car will accelerate and brake. Display the current speed after
#  each acceleration and brake.
# ---------------------------------------------

#Initializes the car class
class Car:
    def __init__(self, eYear, eMake, eSpeed):
        self.year = eYear
        self.make = eMake
        self.speed = eSpeed

    def getYear(self):
        return self.year

    def getMake(self):
        return self.make

    def getSpeed(self):
        return self.speed

    def accelerate(self):
        if ((self.speed + 5) > 120):
            self.speed = 120
        else:
            self.speed = self.speed + 5

    def brake(self):
        if ((self.speed - 5) < 0):
            self.speed = 0
        else:
            self.speed = self.speed - 5

def main():
    
    projectStart()

    accelerateNum = 0
    brakeNum = 0

    year = getYearData("\tEnter the year of the car: ")
    carMake = getStringData("\tEnter the make of the car: ")
    initialSpeed = getIntegerData("\tEnter the initial car speed: ")

    myCar = Car(year, carMake, initialSpeed)

    timesAccelerated = getIntegerData("\tEnter how many times you accelerated: ")
    timesBrake = getIntegerData("\tEnter the amount of times you hit the brakes: ")

    #Acceleration
    print('-' * 50)
    print("Acceleration of 5 mph is applied for each time")
    for ctr in range(timesAccelerated):
        accelerateNum = accelerateNum + 1
        myCar.accelerate()
        print("Accelerate #" , "\t\t" , "Current Speed(mph)")
        print(accelerateNum, "\t\t\t", myCar.getSpeed())

    
    #Brake
    print('-' * 50)
    print("Brake of 5 mph is applied for each time")
    for ctr in range(timesBrake):
        brakeNum = brakeNum + 1
        myCar.brake()
        print("Brake #", "\t\t",  "Current Speed(mph)")
        print(brakeNum, "\t\t\t", myCar.getSpeed())

    display(myCar, accelerateNum, brakeNum)
    projectEnd()


#This function displays the results
def display(myCar, accelerateNum, brakeNum):
    print('-' * 50)
    print("Project Summary: Car Travel Information")
    print("\tFinal Speed of", myCar.getYear(), myCar.getMake(), "is", myCar.getSpeed(), "mph")


#This function makes sure the user enters the proper year
def getYearData(prompt):
    while True:
        try:
            value = int(input(prompt))
            if(value >= 1900 and value <= 2025):
                return value
            else:
                print("Error Message!!! Enter a year between 1900 and 2025")
        except ValueError:
            print("Error Message!!! Enter a year between 1900 and 2025")



# This function will display the start of the project
def projectStart():
    print('Start of Project 9')
    print('Written by: Jaziah Sanders')
    print('Date: November 22nd ')
    print('-' * 50)
    print('\tCar Speed')
    print('-' * 50 + '\n')

# This function will display the end of the project
def projectEnd():
    print('-' * 50)
    print('End of Project 9')


def getIntegerData(prompt):
    while True:
        try:
            value = int(input(prompt))
            if(value <= 0):
                raise ValueError
            else:
                return value
        except ValueError:
            print("Error Message!!!  Enter positive numbers ONLY!")


def getStringData(prompt):
    while True:
        value = input(prompt)
        if value in ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Tesla']:
            return value
        else:
            print("Error Message!!! Please enter a valid car make (Toyota, Honda, Ford, Chevrolet, or Tesla)")


main()