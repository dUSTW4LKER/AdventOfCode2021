from Input.Day3 import day3InputData

def SolveDay3 ():
	input0 = day3InputData.copy()
	input1 = day3InputData.copy()
	input2 = day3InputData.copy()
	
	print ("Day 3.1: " + SolveDay3_1(input0))
	print ("Day 3.2: " + SolveDay3_2(input1, input2))


def SolveDay3_1(input):
	gammaRate = ""
	epsilonRate = ""

	for n in range(0, len(input[0])):
		zeroCount = 0

		for i in input:
			if i[n] == "0":
				zeroCount += 1

		if zeroCount > (len(input)/2):
			gammaRate += "0"
			epsilonRate += "1"
		else:
			gammaRate += "1"
			epsilonRate += "0"

	powerConsumption = int(gammaRate, 2) * int(epsilonRate, 2)

	return (f"{int(gammaRate, 2)} x {int(epsilonRate, 2)} = {powerConsumption}")

def SolveDay3_2 (input0, input1):
	co2ScrubberRating = int(CalculateCo2ScrubberRating(input0), 2)
	oxygenGeneratorRating = int(CalculateOxygenGeneratorRating(input1), 2)
	lifeSupportRating = co2ScrubberRating * oxygenGeneratorRating

	return (f"{ co2ScrubberRating } x { oxygenGeneratorRating } = { lifeSupportRating }")

def CalculateCo2ScrubberRating(input):
	i = 0
	prefix = ""
	
	while len(input) > 1:
		toDelete, addToPrefix = CalculateMostCommonBit(i, input)
		input = [x for x in input if not x.startswith(prefix + toDelete)]
		prefix += addToPrefix
		i += 1

	return (input[0])



def CalculateOxygenGeneratorRating(input):
	i = 0
	prefix = ""
	
	while len(input) > 1:
		addToPrefix, toDelete = CalculateMostCommonBit(i, input)
		input = [x for x in input if not x.startswith(prefix + toDelete)]
		prefix += addToPrefix
		i += 1

	return (input[0])

def CalculateMostCommonBit(position, input):
	zeroCount = 0

	for i in input:
		if i[position] == "0":
			zeroCount += 1

	if zeroCount > (len(input)/2):
		return ("0", "1")

	return ("1", "0")
