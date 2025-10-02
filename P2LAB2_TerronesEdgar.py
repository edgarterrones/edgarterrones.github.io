# Edgar C Terrones
# 10/2/25
# P2LAB2
# Vehicle Calculations

vehicle_mpg = {"Camaro" : 18.21,
                    "Prius" : 52.36,
                    "Model S" : 110,
                    "Silverado" : 26}
keys = vehicle_mpg.keys()

print(keys)

print("Enter a vehicle to see it's MPG:")
selected_vehicle = input()
mpg = vehicle_mpg[selected_vehicle]

print("The", selected_vehicle, "gets", mpg, "mpg.")

print("How many miles will you drive the", selected_vehicle, "?")

miles_driven = float(input())

gallons_needed = miles_driven / mpg

print(f"{gallons_needed:.2f}", "gallon(s) of gas are needed to drive the", selected_vehicle, miles_driven, "miles.")



