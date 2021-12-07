from Input.Day1 import inputMeasurements

def SolveDay1():
	input0 = inputMeasurements.copy()
	input1 = inputMeasurements.copy()
	input2 = inputMeasurements.copy()

	print ("Day 1.1: %d" %SolutionDay1_1(input0))
	print ("Day 1.2: %d" %SolutionDay1_2forloop(input1))
	print ("Day 1.2: %d" %SolutionDay1_2index(input2))

def SolutionDay1_1(input):
	previousInput = input.pop(0)
	n = 0

	for i in input:
		if i > previousInput:
			n += 1
		previousInput = i

	return n

def SolutionDay1_2forloop(input):
	previousInput2 = input.pop(0)
	previousInput1 = input.pop(0)
	previousInput0 = input.pop(0)
	n = 0
	
	for i in input:
		if i > previousInput2:
			n += 1
		previousInput2 = previousInput1
		previousInput1 = previousInput0
		previousInput0 = i

	return n

def SolutionDay1_2index(input):
	n = 0
	for i in range(0, len(input)-3):

		if input[i+3] > input[i]:
			n += 1

	return n
