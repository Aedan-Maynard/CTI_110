#Aedan Maynard
#9/26/26
#P2LAB2





#dictionary of cars and their corresponding mpg
cars ={"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}
#prints the keys for our dictionary of cars for the user to see
keys = cars.keys()

print(keys)

vehicle = input("Enter a vehicle to see its mpg: ")
#recalls the mpg of the vehicle specified by the user and prints it out
mpg = cars[vehicle]
print(f"The {vehicle} gets {mpg} mpg.")

#Float input from users asking how many miles they will drive
miles = float(input(f"How many miles will you drive the {vehicle}? "))

#Calculate the gallons of gassed based on the vehicle and its corresponding mpg
gallons = miles / mpg
#prints the number of gallons of gas needed to travel the specified miles in the specified vehicle
print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles} miles.")