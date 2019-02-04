
milesPerYear = int(input("Please enter how many miles you drive in a year: "))
pricePerGallon = float(input("Please enter how much a gallon of gasoline costs: "))
hybridInitCost = int(input("Please enter how much the hybrid car costs: "))
hybridEfficiency = int(input("Please enter the efficiency of the hybrid in miles per gallon: "))
hybridResale = int(input("Please enter the estimated resale value of the hybrid car after 5 years: "))
gasInitCost = int(input("Please enter how much the gas car costs: "))
gasEfficiency = int(input("Please enter the efficiency of the car in miles per gallon: "))
gasResale = int(input("Please enter the estimated resale value of the gas car after 5 years: "))
preference = input("Do you prefer minimized gas consumption or minimized total cost? ")
def gasConsumed(gas):
	return 5*(milesPerYear/gas)

def totalCost(car, gas, resale):
	total = float(car) + (float(gasConsumed(gas)) * pricePerGallon) - float(resale)
	return total
gasTotal = totalCost(gasInitCost, gasEfficiency, gasResale)
hybridTotal = totalCost(hybridInitCost, hybridEfficiency, hybridResale)

if preference == "gas":
	if gasConsumed(gasEfficiency) > gasConsumed(hybridEfficiency):
		print("The most efficient car is the hybrid.")
	else: print("The most efficient car is the gas car.")
else:
	if gasTotal < hybridTotal:
		print("The gas car is cheaper, with a total cost of $" + str(round(gasTotal)))
	else: print("The hybrid car is cheaper, with a total cost of $" + str(round(hybridTotal)))


