# Simple example of recursion
number = 10
print("Recursion test, T-minus")
def countdown(count):
	while count <= 0:
		print("Blastoff!")
		return
	else:
		print(str(count) + "...")
		count -= 1
		countdown(count)
countdown(number)

bites = 10

def eatPizza(numBites):  #FIXME For some reason the numBites variable isn't decrementing like I thought
	eaten = False
	if numBites == 0:
		eaten = True
		return
	print("Number of bites left: " + str(numBites))
	while eaten == False:
		numBites -= 1
		eatPizza(numBites)
		if numBites == 0:
			eaten = True
			return
	print("All done!")
	return
eatPizza(bites)
		
